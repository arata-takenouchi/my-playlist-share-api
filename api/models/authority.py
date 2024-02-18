from sqlalchemy import Column, String, DateTime, Boolean
from api.db import Base

class Authority(Base):
  __tablename__ = "authority"
  id = Column(String(50), primary_key=True)
  user_id = Column(String(50), nullable=False)
  function_name = Column(String(100), nullable=True)
  permission = Column(Boolean, nullable=True)
  created = Column(DateTime, nullable=False)
  updated = Column(DateTime, nullable=False)
  created_user_id = Column(String(50), nullable=False)
  updated_user_id = Column(String(50), nullable=False)
