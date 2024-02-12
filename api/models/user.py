from sqlalchemy import Column, String, DateTime
from api.db import Base

class User(Base):
  __tablename__ = "user"
  id = Column(String(50), primary_key=True)
  name = Column(String(100), nullable=False)
  email = Column(String(100), nullable=False)
  password = Column(String(100), nullable=False)
  created = Column(DateTime, nullable=False)
  updated = Column(DateTime, nullable=False)
