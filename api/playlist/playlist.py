from fastapi import APIRouter

router = APIRouter()

@router.get("/playlists")
async def get_playlists():
  pass

@router.post("/playlist")
async def create_playlist():
  id = 'ulid'
  pass

@router.put("/playlist")
async def update_playlist(id, mail, password, name):
  param = id
  pass

@router.delete("/playlist")
async def update_playlist(id):
  param = id
  pass