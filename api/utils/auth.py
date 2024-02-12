from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import HTTPException
import jwt
import bcrypt
import os
from dotenv import load_dotenv
import datetime
import api.schemas.user as user_schema
import api.models.user as user_model
import api.utils.utility as utility

load_dotenv()

SECRET_KEY = os.environ['TOKEN_SECRET_KEY']

# ユーザー認証
async def authentication(db: AsyncSession, param: user_schema.PostLoginParams) -> user_schema.PostLoginResponse:
  # 該当ユーザーの検索
  stmt = select(
    user_model.User.id,
    user_model.User.name,
    user_model.User.email,
    user_model.User.password,
    ).where(
      (user_model.User.email == param.email)
    )
  getData: Result = await db.execute(stmt)
  user = getData.first()
  # ユーザーが見つからなかったら終了
  if (user == None):
    raise HTTPException(status_code=401, detail='該当するユーザーが存在しません')

  # パスワードの検証
  checkPassword = user.password
  # バイト型にして検証する
  check = bcrypt.checkpw(param.password.encode('utf-8'), checkPassword.encode('latin-1'))
  # 認証に失敗したら終了
  if (check != True):
    raise HTTPException(status_code=401, detail='パスワードが不正です')

  # トークンを生成してレスポンス
  payload_data = {
    'id': user.id,
    'name': user.name,
    'email': user.email,
    # 有効期限は1日
    'exp': utility.now + datetime.timedelta(days=1)
  }
  token = jwt.encode(
      payload=payload_data,
      key=SECRET_KEY,
      algorithm='HS256'
  )
  return user_schema.PostLoginResponse(token=token)

# 認可
async def authorization(authorization: HTTPAuthorizationCredentials, db: AsyncSession) -> str:
  token = authorization.credentials
  user_id = jwt.decode(token, SECRET_KEY, algorithms='HS256').get('id', None)
  if (user_id == None):
      raise HTTPException(status_code=401, detail='idが不正です')
  stmt = select(
    user_model.User.id,
    ).where(
      (user_model.User.id == user_id)
    )
  getData: Result = await db.execute(stmt)
  user = getData.first()
  # 一度sessionを閉じないと後続のdb処理ができない
  await db.close()
  # ユーザーが見つからなかったら終了
  if (user == None):
    raise HTTPException(status_code=401, detail='該当するユーザーが存在しません')
  # 認可が通ればidを返す
  return user_id
