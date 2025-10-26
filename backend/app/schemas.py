from pydantic import BaseModel
from datetime import datetime

class CustomerOut(BaseModel):
  id: int
  name: str
  email: str | None = None
  created_at: datetime

  class Config:
    from_attributes = True