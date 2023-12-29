from typing import Optional
from pydantic import BaseModel, Field

class Create(BaseModel):
  playlist_link: str = Field(description="プレイリストのURL")
  description: str = Field(description="説明")