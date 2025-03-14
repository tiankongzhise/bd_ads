from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
import os
from dotenv import load_dotenv
from contextlib import contextmanager
from typing import Generator
# 加载环境变量
load_dotenv()

# 获取数据库连接信息
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USERNAME", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME_BDDATA", "baidu_source_data")

# 创建数据库连接URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 获取数据库会话
@contextmanager
def get_db()->  Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
