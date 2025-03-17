from sqlalchemy import Column, Integer, String, DateTime, Text, JSON,inspect,Date,UniqueConstraint,func,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



Base = declarative_base()

class LeadsNoticePush(Base):
    """百度推送线索数据模型"""
    __tablename__ = 'leadsnotice_push'
    __table_args__ = {'schema': 'baidu_source_data'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer,nullable=True,comment='有效性标注')
    ucid = Column(Integer, comment='ucid数值')
    clueId = Column(String(255), comment='clueId字符串')
    commitTime = Column(DateTime, default=datetime.now, comment='commitTime时间时分秒')
    solutionTypeName = Column(String(255), comment='solutionTypeName字符串')
    cluePhoneNumber = Column(String(75), comment='cluePhoneNumber字符串')
    flowChannelName = Column(String(255), comment='flowChannelName字符串')
    formDetail = Column(JSON, comment='formDetail是JsonArray')
    imName = Column(String(255), comment='imName字符串')
    clueUserMsgCount = Column(Integer, comment='clueUserMsgCount数值')
    humanServiceMsgCount = Column(Integer, comment='humanServiceMsgCount数值')
    aiServiceMessageNum = Column(Integer, comment='aiServiceMessageNum数值')
    ip = Column(String(50), comment='ip字符串')
    wechatAccount = Column(String(255), comment='wechatAccount字符串')
    url = Column(Text, comment='url字符串')
    consultUrl = Column(Text, comment='consultUrl字符串')
    created_at = Column(DateTime, default=datetime.now, comment='创建时间')
    
    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }
    def __repr__(self):
        return f"<LeadsNoticePush(id={self.id}, clueId={self.clueId})>"

class BaiduAccoutCostRrport(Base):
    """百度账户日消费数据"""
    __tablename__ = 'baidu_accout_cost_report'
    __table_args__ = (
        UniqueConstraint('date', 'userId', name='uq_date_user_id'),
        {'schema': 'baidu_source_data'})
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, default=datetime.now, comment='日期时间')
    userName = Column(String(255), comment='用户名')
    userId = Column(Integer, comment='用户id')
    product = Column(String(255), comment='投放渠道')
    impression = Column(Integer, comment='展现量')
    click = Column(Integer, comment='点击量')
    cost = Column(DECIMAL(8,2), comment='消费金额')
    created_at = Column(DateTime,default=func.now(),comment='记录创建时间')
    updated_at = Column(DateTime,onupdate=func.now(),comment='记录更新时间')
    
    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }
    def __repr__(self):
        return f"<BaiduAccoutCostRrport(userId={self.userId}, userName={self.userName},date={self.date},cost = {self.cost},created_at={self.created_at})>"
    
