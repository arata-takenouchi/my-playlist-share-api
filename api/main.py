from fastapi import FastAPI
from api.login import login
from api.playlist import playlist
from api.user import user

app = FastAPI()
app.include_router(login.router)
app.include_router(playlist.router)
app.include_router(user.router)

@app.get("/hello")
async def hello():
  return{"message": "hello world"}