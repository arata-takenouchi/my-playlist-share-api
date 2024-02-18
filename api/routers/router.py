from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.schemas.playlist as playlist_schema
import api.schemas.user as user_schema
import api.schemas.authority as authority_schema
import api.cruds.crud as crud
import api.utils.auth as auth

router = APIRouter()

@router.post("/user/login", response_model=user_schema.PostLoginResponse)
async def authentication(param: user_schema.PostLoginParams , db: AsyncSession = Depends(get_db)):
  return await auth.authentication(db, param)

@router.post("/playlist")
async def create_playlist(param: playlist_schema.PostParams, authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: AsyncSession = Depends(get_db)):
  user_id = await auth.authorization(authorization, db)
  await auth.check_user_permission(authority_schema.GetParams(user_id=user_id, function_name='playlist.post'), db)
  return await crud.create_playlist(playlist_schema.PostParamsForDB(**dict(param), user_id=user_id), db)
