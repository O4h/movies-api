from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database import models, crud, schemas
from api.database.sql_connection import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies", response_model=List[schemas.Movie])
def get_movies(limit: int = 100, db: Session = Depends(get_database)):
    return crud.get_movies(db, limit=limit)


@app.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_database)):
    return crud.create_movie(db, movie=movie)


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(get_database)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.put("/movies/{movie_id}", response_model=schemas.Movie)
def edit_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_database)):
    existing_movie = crud.get_movie(db, movie_id)
    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.update_movie(db, movie_id, movie=movie)


@app.delete("/movies/{movie_id}", response_model=schemas.Movie)
def remove_movie(movie_id: int, db: Session = Depends(get_database)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.remove_movie(db, movie_id)
