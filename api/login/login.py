from fastapi import APIRouter

router = APIRouter()

# ここはauthの仕組みをなにか使ってみてもいいかも
@router.get("/get")
async def login(mail, password):
  pass