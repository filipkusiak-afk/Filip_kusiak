from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Tworzymy plik bazy danych 'movies.db'
db_url = 'sqlite:///movies.db'
engine = create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Definicja tabeli Filmów
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True) # ID filmu
    title = Column(String)                             # Tytuł
    genres = Column(String)                            # Gatunki

    # Metoda do zamiany obiektu na słownik (potrzebne w API)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genres": self.genres
        }

# Funkcja tworząca tabele
def create_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db()
    print("Baza danych utworzona!")