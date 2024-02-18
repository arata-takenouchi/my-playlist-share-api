from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import bcrypt
import api.models.playlist as playlist_model
import api.models.user as user_model
import api.models.authority as authority_model
import api.utils.utility as utility
from api.db import Base

DB_URL = "mysql+pymysql://root@db:3306/my_playlist_share?charset=utf8"
engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(
  autocommit=False, autoflush=False, bind=engine, class_=Session,
)
salt = bcrypt.gensalt(10)
  # hash関数にpasswordをバイト型にして渡す必要がある
hash1 = bcrypt.hashpw('test_user_password_1'.encode('utf-8'), salt)
hash2 = bcrypt.hashpw('test_user_password_2'.encode('utf-8'), salt)
hash3 = bcrypt.hashpw('test_user_password_3'.encode('utf-8'), salt)
# テストデータ
userList=[
  user_model.User(id='test_user_id_1', email='test_user_email_1', name='test_user_name_1', password=hash1, created=utility.now, updated=utility.now),
  user_model.User(id='test_user_id_2', email='test_user_email_2', name='test_user_name_2', password=hash2, created=utility.now, updated=utility.now),
  user_model.User(id='test_user_id_3', email='test_user_email_3', name='test_user_name_3', password=hash3, created=utility.now, updated=utility.now),
]

authorityList=[
  authority_model.Authority(id='test_authority_id_1', user_id='test_user_id_1', function_name='playlist.post', permission=1, created=utility.now, updated=utility.now, created_user_id='test_user_id_1', updated_user_id='test_user_id_1'),
  authority_model.Authority(id='test_authority_id_2', user_id='test_user_id_2', function_name='playlist.post', permission=0, created=utility.now, updated=utility.now, created_user_id='test_user_id_1', updated_user_id='test_user_id_1'),
]

def reset_database():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

def add_database():
  with Session.begin() as session:
    session.add_all(userList)
    session.add_all(authorityList)
    session.commit()
    session.close()

if __name__ == "__main__":
  reset_database()
  add_database()
