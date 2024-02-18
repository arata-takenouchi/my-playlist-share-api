from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class PostParams(BaseModel):
  playlist_name: str = Field(description="プレイリストの名前")
  playlist_link: str = Field(description="プレイリストのURL")
  comment: str = Field(description="説明")
  # playlist_image: str = Field(description="プレイリストの画像")

class PostParamsForDB(PostParams):
  user_id: str

class GetParams(BaseModel):
  playlist_name: Optional[str] = Field(None, description="プレイリストの名前")

class GetResponse(BaseModel):
  id: str = Field(description="id ulid")
  playlist_name: str = Field(description="プレイリストの名前")
  playlist_link: str = Field(description="プレイリストのURL")
  comment: str = Field(description="説明")
  created: datetime = Field(description="作成日時 YYYY-MM-DD hh:mm:ss")
  updated: datetime = Field(description="更新日時 YYYY-MM-DD hh:mm:ss")
  created_user_id: str = Field(description="作成ユーザーID")
  updated_user_id: str = Field(description="更新ユーザーID")
  user_id: str = Field(description="対象ユーザーID")
