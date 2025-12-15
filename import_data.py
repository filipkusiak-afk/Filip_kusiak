import csv
import os
from models import SessionLocal, Movie, create_db

def load_movies_local():
    # 1. Tworzymy tabele w bazie (jeśli nie istnieją)
    create_db()
    
    session = SessionLocal()

    # Sprawdzamy, czy baza nie jest już pełna
    if session.query(Movie).count() > 0:
        print("Baza już zawiera dane. Pomijam import.")
        session.close()
        return

    # Sprawdzamy czy plik CSV fizycznie istnieje
    if not os.path.exists("movies.csv"):
        print("BŁĄD: Nie znaleziono pliku 'movies.csv' w tym folderze!")
        return

    print("Rozpoczynam importowanie z pliku lokalnego 'movies.csv'...")

    try:
        # 2. Otwieramy plik z dysku
        with open('movies.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Pomijamy nagłówek (pierwszą linię)
            
            counter = 0
            for row in reader:
                # row[0] -> movieId, row[1] -> title, row[2] -> genres
                movie = Movie(id=int(row[0]), title=row[1], genres=row[2])
                session.add(movie)
                counter += 1
            
            # 3. Zapisujemy wszystko do bazy na raz
            session.commit()
            print(f"SUKCES! Dodano {counter} filmów do bazy 'movies.db'.")

    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    load_movies_local()