from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.schemas.playlist as playlist_schema
import api.cruds.crud as crud

router = APIRouter()

@router.post("/playlist")
async def create_playlist(param: playlist_schema.Create, db: AsyncSession = Depends(get_db)):
  return await crud.create_playlist(param, db)

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