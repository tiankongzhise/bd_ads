# 标准库模块
from datetime import datetime
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
    func, text,
    # 引擎与连接
    create_engine,
    # ORM 基础组件
    Column, inspect
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# 方言特定类型（按需使用）
from sqlalchemy.dialects.mysql import INTEGER  # MySQL 大整数类型

# 异常类
from sqlalchemy.exc import IntegrityError

# 加在配置文件
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class BdAdMaterialTransferTable(Base):
    __tablename__ = 'ads_material_transfer'  # 表名
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    source_user_id = Column(String(64), nullable=False, comment='来源用户ID')
    material_id = Column(String(64), nullable=True, comment='物料ID')
    material_url = Column(String(512), nullable=True, comment='物料URL')
    material_name = Column(String(256), nullable=True, comment='物料名称')
    description = Column(JSON, nullable=True, comment='描述')
    target_user_id = Column(String(64), nullable=False, comment='目标用户ID')
    target_material_id = Column(String(64), nullable=True, comment='目标物料ID')
    target_material_url = Column(String(512), nullable=True, comment='目标物料URL')
    target_material_name = Column(String(256), nullable=True, comment='目标物料名称')
    target_description = Column(JSON, nullable=True, comment='目标描述')
    migrate_status = Column(String(64), nullable=False, comment='迁移状态')
    migrate_time = Column(DateTime, default=datetime.now, comment='迁移时间')
    tableUpdateTime = Column(DateTime,default=func.now(), onupdate=func.now(),comment='记录更新时间')
    
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_0900_ai_ci',
        'mysql_row_format': 'DYNAMIC',
    }
    
    
    def __repr__(self):
        # 获取所有类属性（过滤掉特殊方法）
        class_attrs = [
            f"{attr}={value!r}" 
            for attr, value in self.__class__.__dict__.items() 
            if not attr.startswith('__') and not callable(value)
        ]
        return f"<{self.__class__.__name__}({', '.join(class_attrs)})>"

class BdAdCenterBindTable(Base):
    __tablename__ = 'ads_center_bind'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    center_id = Column(String(64), nullable=False, comment='中心ID')
    center_name = Column(String(64), nullable=False, comment='中心名称')
    user_id = Column(String(64), nullable=False, comment='用户ID')
    user_name = Column(String(64), nullable=False, comment='用户名')
    tableUpdateTime = Column(DateTime,default=func.now(), onupdate=func.now(),comment='记录更新时间')
    __table_args__ = (
        UniqueConstraint('center_id', 'user_id', name='uq_center_id_user_id'),
        {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_0900_ai_ci',
        'mysql_row_format': 'DYNAMIC',
        
    }
                      )

class BdServiceDb(object):
    def __init__(self):
        # 修正环境变量获取方式
        self.db_host = os.getenv("DB_HOST", "数据库地址未设置")
        self.db_port = int(os.getenv("DB_PORT", 3306))   
        self.db_username = os.getenv("DB_USERNAME", "")
        self.db_password = os.getenv("DB_PASSWORD", "")
        self.db_name = os.getenv("DB_NAME_SERVICE", "")

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
