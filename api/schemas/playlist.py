from typing import Optional
from pydantic import BaseModel, Field

class PostParams(BaseModel):
  playlist_name: str = Field(description="プレイリストの名前")
  playlist_link: str = Field(description="プレイリストのURL")
  comment: str = Field(description="説明")
  # playlist_image: str = Field(description="プレイリストの画像")

class PostParamsForDB(PostParams):
  user_id: str
