import csv
from typing import List
from fastapi import FastAPI

app = FastAPI()


# --- ZADANIE 1: Endpoint 'hello': 'world' [cite: 15] ---
@app.get("/")
def read_root():
    return {"hello": "world"}


# --- ZADANIE 2: Klasa Movie i endpoint /movies [cite: 16, 17, 18] ---

class Movie:
    def __init__(self, movie_id, title, genres):
        self.id = movie_id
        self.title = title
        self.genres = genres

    # Metoda pomocnicza do serializacji (choć FastAPI robi to automatycznie,
    # zadanie wymaga użycia __dict__ [cite: 21])
    def to_dict(self):
        return self.__dict__


@app.get("/movies")
def get_movies():
    results = []
    # Pobranie danych z pliku [cite: 17]
    try:
        with open('movies.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Pominięcie nagłówka

            # Iteracja po wierszach i tworzenie obiektów [cite: 20]
            for row in reader:
                # Zakładamy strukturę pliku: movieId, title, genres
                movie = Movie(row[0], row[1], row[2])

                # Serializacja obiektu za pomocą metody magicznej __dict__ [cite: 21]
                results.append(movie.to_dict())

        # Zwrócenie listy zserializowanych obiektów [cite: 22]
        return results
    except FileNotFoundError:
        return {"error": "Plik movies.csv nie został znaleziony."}


# --- ZADANIE 3 i 4: Modele i endpointy dla links, ratings, tags [cite: 52, 53] ---

# --- LINKS ---
class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movieId = movie_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id


@app.get("/links")  # [cite: 54]
def get_links():
    results = []
    try:
        with open('links.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                # Zakładamy strukturę: movieId, imdbId, tmdbId
                # Obsługa brakujących danych (np. brak tmdbId)
                tmdb = row[2] if len(row) > 2 else None
                link = Link(row[0], row[1], tmdb)
                results.append(link.__dict__)
        return results
    except FileNotFoundError:
        return {"error": "Plik links.csv nie został znaleziony."}


# --- RATINGS ---
class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp


@app.get("/ratings")  # [cite: 55]
def get_ratings():
    results = []
    try:
        # Uwaga: ratings.csv bywa duży, wczytujemy tylko pierwsze 100 dla przykładu
        # aby przeglądarka się nie zawiesiła
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


# --- TAGS ---
class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp


@app.get("/tags")  # [cite: 56]
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