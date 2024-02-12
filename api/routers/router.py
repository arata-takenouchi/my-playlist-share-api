from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.schemas.playlist as playlist_schema
import api.schemas.user as user_schema
import api.cruds.crud as crud
import api.utils.auth as auth

router = APIRouter()

@router.post("/user/login", response_model=user_schema.PostLoginResponse)
async def authentication(param: user_schema.PostLoginParams , db: AsyncSession = Depends(get_db)):
  return await auth.authentication(db, param)

@router.post("/playlist")
async def create_playlist(param: playlist_schema.PostParams, authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: AsyncSession = Depends(get_db)):
  user_id = await auth.authorization(authorization, db)
  return await crud.create_playlist(playlist_schema.PostParamsForDB(**dict(param), user_id=user_id), db)

# @router.get("/login")
# async def login(mail, password):
#   pass

# @router.get("/playlists")
# async def get_playlists():
#   pass

# @router.get("/user")
# async def get_user(id):
#   param = id
#   pass

# @router.get("/users")
# async def get_users():
#   pass

# @router.post("/user")
# async def create_user():
#   id = 'ulid'
#   pass

# @router.put("/playlist")
# async def update_playlist(id, mail, password, name):
#   param = id
#   pass

# @router.put("/playlist")
# async def update_playlist(id, title, link, description, user_name):
#   create_date = ''
#   pass

# @router.delete("/playlist")
# async def update_playlist(id):
#   param = id
#   pass

# @router.delete("/user")
# async def delete_playlist(id):
#   param = id
#   pass