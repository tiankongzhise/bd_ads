# 标准库模块
import os
import logging
from typing import Generator
from contextlib import contextmanager

# SQLAlchemy 核心及ORM组件
from sqlalchemy import (
    # 数据类型
    Integer, String, Text, DateTime, JSON,
    # 表结构约束
    PrimaryKeyConstraint, UniqueConstraint,
    # 函数与SQL表达式
    func, create_engine,
    # ORM 基础组件
    Column
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# 方言特定类型（按需使用）
from sqlalchemy.dialects.mysql import INTEGER  # MySQL 大整数类型

# 异常类

# 加在配置文件
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
Base = declarative_base()

class BdAuthTokenTable(Base):
    __tablename__ = 'bd_auth_token_new'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_0900_ai_ci',
        'mysql_row_format': 'DYNAMIC'
    }

    # key = Column(
    #     Integer().with_variant(Integer(unsigned=True), "mysql"),
    #     primary_key=True,
    #     autoincrement=True,
    #     comment='自增主键'
    # )
    key = Column(
        Integer().with_variant(INTEGER(unsigned=True), "mysql"),  # 修正这里
        primary_key=True,
        autoincrement=True,
        comment='自增主键'
    )
    userId = Column(
        String(32),
        default='',
        server_default='',
        unique=True,
        comment='用户ID'
    )
    openId = Column(
        String(32),
        default='',
        server_default='',
        unique=True,
        comment='授权用户查询标识'
    )
    refreshToken = Column(
        Text,
        nullable=True,
        comment='刷新令牌'
    )
    accessToken = Column(
        Text,
        nullable=True,
        comment='访问令牌'
    )
    expiresTime = Column(
        DateTime,
        nullable=True,
        comment='访问令牌过期时间'
    )
    refreshExpiresTime = Column(
        DateTime,
        nullable=True,
        comment='刷新令牌过期时间'
    )
    tableUpdateTime = Column(
        DateTime,
        default=func.now(), 
        onupdate=func.now(),
        comment='记录更新时间'
    )


class OauthDb(object):
    def __init__(self):
        # 修正环境变量获取方式
        self.db_host = os.getenv("DB_HOST", "数据库地址未设置")
        self.db_port = int(os.getenv("DB_PORT", 3306))   
        self.db_username = os.getenv("DB_USERNAME", "")
        self.db_password = os.getenv("DB_PASSWORD", "")
        self.db_name = os.getenv("DB_NAME_OAUTH", "")   

        # 修正SQL连接字符串使用实例变量
        SQLALCHEMY_DATABASE_URL = (
            f"mysql+pymysql://{self.db_username}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}?charset=utf8mb4"
        )
        
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            pool_pre_ping=True,
            pool_recycle=3600
        )
        
        self.SessionLocal = sessionmaker(
            autocommit=False, 
            autoflush=False, 
            bind=self.engine
        )

        # 添加表创建重试机制
        retries = 3
        for _ in range(retries):
            try:
                Base.metadata.create_all(bind=self.engine)
                break
            except Exception as e:
                print(f"Error creating tables: {e}")
                if _ == retries - 1:
                    raise RuntimeError("Failed to create tables after multiple attempts")

    # 添加会话管理方法
    @contextmanager
    def get_session(self) ->  Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
            
            
    def dynamic_update(self, model, data):
        """带自动会话管理的更新方法"""
        with self.SessionLocal() as session:
            try:
                table = model.__table__
                
                # 获取所有唯一约束（包含主键和unique=True的列）
                unique_constraints = [
                    constraint
                    for constraint in table.constraints
                    if isinstance(constraint, (PrimaryKeyConstraint, UniqueConstraint))
                ]
    
                # 收集所有约束字段组合
                required_combinations = []
                for constraint in unique_constraints:
                    columns = [col.name for col in constraint.columns]
                    required_combinations.append(columns)
    
                # 校验必须包含至少一个完整约束
                valid_update = any(
                    all(col in data for col in columns)
                    for columns in required_combinations
                )
    
                if not valid_update:
                    raise ValueError(
                        f"必须包含以下任一完整约束字段组合: {required_combinations}"
                    )
    
                # === 增强版类型校验逻辑 ===
                type_check_errors = []
                for col_name, value in data.items():
                    col = getattr(model, col_name, None)
                    if not col:
                        continue  # 忽略不存在的字段
                    
                    # 获取列定义类型和数据库类型
                    col_type = col.type.python_type
                    db_type = str(col.type).lower()
    
                    # 处理日期时间类型转换
                    if isinstance(value, str) and 'datetime' in db_type:
                        try:
                            # 支持多种日期格式解析
                            from dateutil.parser import parse
                            data[col_name] = parse(value)
                        except (ValueError, TypeError) as e:
                            type_check_errors.append(
                                f"日期字段 '{col_name}' 格式错误: {value} (示例有效格式: '2023-01-01 12:00:00')"
                            )
                        continue
                    
                    # 跳过JSON类型的校验
                    if isinstance(col.type, JSON):
                        continue
                    
                    # 类型校验
                    if not isinstance(value, col_type):
                        try:
                            # 尝试强制类型转换
                            data[col_name] = col_type(value)
                        except (ValueError, TypeError):
                            type_check_errors.append(
                                f"字段 '{col_name}' 类型不匹配，期望 {col_type.__name__}，实际值 '{value}'"
                            )
    
                if type_check_errors:
                    raise ValueError("\n".join(type_check_errors))
                # === 结束新增逻辑 ===
                # 分离查询条件与更新数据
                condition = {
                    col: data[col] 
                    for columns in required_combinations 
                    for col in columns 
                    if col in data
                }
                update_data = {k: v for k, v in data.items() if k not in condition}

    
                if not update_data:
                    raise ValueError("没有需要更新的字段")
                
                result = session.query(model).filter_by(**condition).first()
                if result is None:
                    # 执行新增
                    updated_count = (
                        session.add(model(**data))
                    )
                    # logger.error(f'新增账户id:{data['userId']}的Oauth信息')
                    print(f'新增账户id:{data['userId']}的Oauth信息')
                else:
                    # 执行更新
                    updated_count = (
                        session.query(model)
                        .filter_by(**condition)
                        .update(update_data, synchronize_session=False)
                    )
                    # logger.error(f'更新账户id:{data['userId']}的Oauth信息')
                    print(f'更新账户id:{data['userId']}的Oauth信息')
                session.commit()
                return updated_count
            except Exception as e:
                session.rollback()
                raise RuntimeError(f"数据完整性错误: {str(e)}") from e
