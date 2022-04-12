from pydantic import BaseModel


class MovieCreate(BaseModel):
    name: str
    publication_year: int
    description: str


class Movie(MovieCreate):
    id: int

    class Config:
        orm_mode = True
