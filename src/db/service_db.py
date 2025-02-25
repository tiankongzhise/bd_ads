# 标准库模块
from datetime import datetime
import os
import logging

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
