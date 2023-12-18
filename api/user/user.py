from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def get_user(id):
  param = id
  pass

@router.get("/users")
async def get_users():
  pass

@router.post("/user")
async def create_user():
  id = 'ulid'
  pass

@router.put("/playlist")
async def update_playlist(id, title, link, description, user_name):
  create_date = ''
  pass

@router.delete("/user")
async def delete_playlist(id):
  param = id
  pass