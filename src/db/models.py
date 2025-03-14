from sqlalchemy import Column, Integer, String, DateTime, Text, JSON,inspect
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
