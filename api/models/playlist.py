from sqlalchemy import Column, Integer, String, DateTime
from api.db import Base

class Playlist(Base):
  __tablename__ = "playlist"
  id = Column(Integer, primary_key=True, autoincrement=True)
  playlist_link = Column(String, nullable=False)
  description = Column(String, nullable=False)
  created = Column(DateTime, nullable=False)
  updated = Column(DateTime, nullable=False)
  created_user_id = Column(String, nullable=False)
  updated_user_id = Column(String, nullable=False)