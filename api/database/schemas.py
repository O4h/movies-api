import datetime
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    publication_date: datetime.date()
    description: str

    class Config:
        orm_mode = True