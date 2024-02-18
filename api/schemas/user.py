from pydantic import BaseModel, Field
from datetime import datetime

class PostParams(BaseModel):
  name: str = Field(description="ユーザー名")
  email: str = Field(description="メールアドレス")
  password: str = Field(description="パスワード")

# class PostResponse(BaseModel):
#   id: str = Field(description="id ulid")
#   name: str = Field(description="ユーザー名")
#   email: str = Field(description="メールアドレス")
#   created: datetime = Field(description="作成日時 YYYY-MM-DD hh:mm:ss")
#   updated: datetime = Field(description="更新日時 YYYY-MM-DD hh:mm:ss")

class PostLoginParams(BaseModel):
  email: str = Field(description="メールアドレス")
  password: str = Field(description="パスワード")

class PostLoginResponse(BaseModel):
  token: str = Field(description="認証トークン")
