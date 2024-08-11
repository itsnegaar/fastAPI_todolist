from pydantic import BaseModel, Field
from datetime import datetime


class Todo(BaseModel):
    title: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    done: bool



