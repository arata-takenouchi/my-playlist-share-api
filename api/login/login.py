from fastapi import APIRouter

router = APIRouter()

# ここはauthの仕組みをなにか使ってみてもいいかも
@router.get("/login")
async def login(mail, password):
  pass