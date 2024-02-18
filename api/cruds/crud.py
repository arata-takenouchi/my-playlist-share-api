from typing import List, Union
from sqlalchemy import select, bindparam
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from ulid import ULID
import bcrypt
import api.models.playlist as playlist_model
import api.schemas.playlist as playlist_schema
import api.models.user as user_model
import api.schemas.user as user_schema
import datetime
import api.utils.utility as utility

# 今日の日付を保持
timedelta = datetime.timedelta(hours=9)
JST = datetime.timezone(timedelta, 'JST')
now = datetime.datetime.now(JST)
# YYYY-MM-DD
currentDate = now.strftime('%Y-%m-%d')
# YYYY-MM-DD H:M:S
currentDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# H:M:S
currentTime = now.strftime('%H:%M:%S')

async def post_user(param: user_schema.PostParams, db: AsyncSession):
  # パスワードはハッシュ化して保存する
  salt = bcrypt.gensalt(10)
  # hash関数にpasswordをバイト型にして渡す必要がある
  hash = bcrypt.hashpw(param.password.encode('utf-8'), salt)
  param.password = hash
  postData = user_model.User(
    **dict(param),
    id = ULID(),
    created = utility.current_date_str(),
    updated = utility.current_date_str(),
  )
  db.add(postData)
  await db.commit()
  await db.refresh(postData)
  await db.close()

async def post_playlist(param: playlist_schema.PostParamsForDB, db: AsyncSession):
  postData = playlist_model.Playlist(
    **dict(param),
    id = ULID(),
    created = utility.current_date_str(),
    updated = utility.current_date_str(),
    created_user_id = param.user_id,
    updated_user_id = param.user_id,
  )
  db.add(postData)
  await db.commit()
  await db.refresh(postData)
  await db.close()

async def get_playlist(db: AsyncSession, param: playlist_schema.GetParams) -> List[playlist_schema.GetResponse]:
  stmt = select(
    playlist_model.Playlist.id,
    playlist_model.Playlist.playlist_name,
    playlist_model.Playlist.playlist_link,
    playlist_model.Playlist.comment,
    playlist_model.Playlist.created,
    playlist_model.Playlist.updated,
    playlist_model.Playlist.created_user_id,
    playlist_model.Playlist.updated_user_id,
    playlist_model.Playlist.user_id,
    )
  if (param.playlist_name != None):
    stmt = stmt.where(
      (playlist_model.Playlist.playlist_name.contains(bindparam('playlist_name')))
    )
  getDataList: Result = await db.execute(stmt, { 'playlist_name': param.playlist_name })
  return getDataList.all()
