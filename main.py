from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
import csv

# Importujemy naszą konfigurację bazy i model Movie z pliku models.py
from models import SessionLocal, Movie

app = FastAPI()

# --- Dependency (Wymagane do połączenia z bazą danych) ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ZADANIE 1: Hello World ---
@app.get("/")
def read_root():
    return {"hello": "world"}

# --- ZADANIE 3: Endpoint /movies korzystający z SQLite (POPRAWIONE) ---
@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    """
    Pobiera listę filmów prosto z bazy danych SQLite.
    """
    #  Pobieramy obiekty z bazy zamiast czytać plik
    movies_from_db = db.query(Movie).all()
    
    # Zamieniamy je na słowniki używając metody to_dict(), którą masz w models.py
    return [movie.to_dict() for movie in movies_from_db]


# --- POZOSTAŁE ENDPOINTY KORZYSTAJĄCE Z PLIKÓW CSV ---

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

@app.get("/ratings")
def get_ratings():
    results = []
    try:
        
        with open('ratings.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            count = 0
            for row in reader:
                rating = Rating(row[0], row[1], row[2], row[3])
                results.append(rating.__dict__)
                count += 1
                if count >= 100: break
        return results
    except FileNotFoundError:
        return {"error": "Plik ratings.csv nie został znaleziony."}

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp

@app.get("/tags")
def get_tags():
    results = []
    try:
        with open('tags.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                tag = Tag(row[0], row[1], row[2], row[3])
                results.append(tag.__dict__)
        return results
    except FileNotFoundError:
        return {"error": "Plik tags.csv nie został znaleziony."}