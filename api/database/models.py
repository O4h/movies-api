from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Date

from api.database.sql_connection import Base


class Movie(Base):
    """"
    Data class representing a movie.
    """
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), index=True)
    publication_year = Column(Integer, index=True)
    description = Column(String(1000))
