from typing import List, Union, Optional
from pydantic import BaseModel, Field

class GetParams(BaseModel):
  user_id: str
  # 「テーブル名.メソッド名」の形式
  # 例：attendance.get
  function_name: str

class GetResponse(BaseModel):
  user_id: str = Field(description="ユーザーid")
  function_name: str = Field(description="権限のあるリクエスト 「テーブル名.リクエストメソッド」")
  permission: bool = Field(description="権限保有の有無")
