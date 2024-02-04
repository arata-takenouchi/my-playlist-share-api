from typing import Optional, Tuple
from sqlalchemy import text, update
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession
import api.models.playlist as playlist_model
import api.schemas.playlist as playlist_schema
import datetime

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

async def create_playlist(param: playlist_schema.Create, db: AsyncSession):
  print(param)
  postData = playlist_model.Playlist(
    **dict(param),
    created = currentDate,
    updated = currentDate,
    created_user_id = 'ulid',
    updated_user_id = 'ulid',
  )
  db.add(postData)
  await db.commit()
  await db.refresh(postData)
