from fastapi import FastAPI
from api.routers import router

app = FastAPI()
app.include_router(router.router)

@app.get("/hello")
async def hello():
  return{"message": "hello world"}