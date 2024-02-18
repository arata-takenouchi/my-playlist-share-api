from sqlalchemy.ext.asyncio import AsyncSession
import api.models.playlist as playlist_model
import api.schemas.playlist as playlist_schema
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

async def create_playlist(param: playlist_schema.PostParamsForDB, db: AsyncSession):
  postData = playlist_model.Playlist(
    **dict(param),
    created = utility.current_date_str(),
    updated = utility.current_date_str(),
    created_user_id = param.user_id,
    updated_user_id = param.user_id,
  )
  db.add(postData)
  await db.commit()
  await db.refresh(postData)
  await db.close()
