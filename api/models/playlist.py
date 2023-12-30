from sqlalchemy import Column, Integer, String, DateTime, Text
from api.db import Base

class Playlist(Base):
  __tablename__ = "playlist"
  id = Column(Integer, primary_key=True, autoincrement=True)
  playlist_link = Column(String(100), nullable=False)
  description = Column(Text, nullable=False)
  created = Column(DateTime, nullable=False)
  updated = Column(DateTime, nullable=False)
  created_user_id = Column(String(50), nullable=False)
  updated_user_id = Column(String(50), nullable=False)