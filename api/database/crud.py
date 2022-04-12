from typing import List

from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schemas


def get_movie(db: Session, movie_id: int) -> models.Movie:
    """
    Return a movie by id

    Parameters
    ----------
    db : Session
        SQLAlchemy session
    movie_id : int
        Movie id
    """
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def get_movies(db: Session, limit: int = 100) -> List[models.Movie]:
    """"
    Return a list of movies

    Parameters
    ----------
    db : Session
        SQLAlchemy session
    limit : int
        Limit of movies to return
    """
    return db.query(models.Movie).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieCreate) -> models.Movie:
    """
    Create a new movie entry

    Parameters
    ----------
    db : Session
        SQLAlchemy session
    movie : schemas.MovieCreate
        Movie information
    """
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie_id: int, movie: schemas.MovieCreate) -> models.Movie:
    """
    Update a movie entry

    Parameters
    ----------
    db : Session
        SQLAlchemy session
    movie_id : int
        Movie id
    movie : schemas.MovieUpdate
        Movie information
    """
    db_movie = get_movie(db, movie_id)
    update(models.Movie).where(models.Movie.id == movie_id).values(**movie.dict())
    db.commit()
    db.refresh(db_movie)
    return db_movie


def remove_movie(db: Session, movie_id: int) -> models.Movie:
    """
    Remove a movie entry

    Parameters
    ----------
    db : Session
        SQLAlchemy session
    movie_id : int
        Movie id
    """
    db_movie = get_movie(db, movie_id)
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie
