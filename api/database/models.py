from sqlalchemy import String, Column, Integrer, Date

from .sql_connection import Base

class Movie(Base):
    """"
    Data class representing a movie.
    """
    __tablename__ = "movies"

    id = Column(Integrer, primary_key=True, index=True)
    name = Column(String, index=True)
    publication_date = Column(Date, index=True)
    description = Column(String)
