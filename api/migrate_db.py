from sqlalchemy import create_engine
import api.models.playlist as playlist_model
import api.models.user as user_model
import api.utils.utility as utility
from sqlalchemy.orm import sessionmaker, Session
from api.db import Base


DB_URL = "mysql+pymysql://root@db:3306/my_playlist_share?charset=utf8"
engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(
  autocommit=False, autoflush=False, bind=engine, class_=Session,
)
# テストデータ
userList=[
  user_model.User(id='test_user_id_1', email='test_user_email_1', name='test_user_name_1', password='test_user_password_1', created=utility.now, updated=utility.now),
  user_model.User(id='test_user_id_2', email='test_user_email_2', name='test_user_name_2', password='test_user_password_2', created=utility.now, updated=utility.now),
  user_model.User(id='test_user_id_3', email='test_user_email_3', name='test_user_name_3', password='test_user_password_3', created=utility.now, updated=utility.now),
]

def reset_database():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

def add_database():
  with Session.begin() as session:
    session.add_all(userList)
    session.commit()
    session.close()

if __name__ == "__main__":
  reset_database()
  add_database()
