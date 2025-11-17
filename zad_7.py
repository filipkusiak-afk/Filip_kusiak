# main.py (lub zad_7_8.py)
import requests
import argparse
from typing import List, Dict, Any, Optional


# --- 7. Implementacja klasy Brewery z typowaniem i __str__ ---

class Brewery:
    """Klasa reprezentująca pojedynczy browar pobrany z Open Brewery DB API."""

    # Atrybuty z typowaniem zgodnym z API (z wybranymi kluczowymi polami)
    id: str
    name: str
    brewery_type: str
    street: Optional[str] = None  # Używamy Optional, bo niektóre mogą być None
    city: str
    state: Optional[str] = None
    postal_code: str
    country: str
    phone: Optional[str] = None
    website_url: Optional[str] = None

    def __init__(self, data: Dict[str, Any]):
        """Inicjalizuje obiekt Brewery na podstawie słownika danych z API."""
        self.id = data.get('id', 'N/A')
        self.name = data.get('name', 'N/A')
        self.brewery_type = data.get('brewery_type', 'N/A')
        self.street = data.get('street')
        self.city = data.get('city', 'N/A')
        self.state = data.get('state')
        self.postal_code = data.get('postal_code', 'N/A')
        self.country = data.get('country', 'N/A')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')

    def __str__(self) -> str:
        """Zwraca czytelny opis obiektu."""
        address = f"{self.street}, {self.postal_code} {self.city}, {self.country}"
        phone_info = f" | Tel: {self.phone}" if self.phone else ""
        web_info = f" | Web: {self.website_url}" if self.website_url else ""

        return f"🍺 Browar: {self.name} ({self.brewery_type.upper()})\n" \
               f"   Adres: {address}\n" \
               f"   Info: {phone_info}{web_info}"


# --- Funkcja główna skryptu ---

def fetch_breweries(city: Optional[str] = None) -> List[Brewery]:
    """
    Pobiera dane o browarach z API.
    Ogranicza do 20 wyników lub do podanego miasta.
    """
    base_url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if city:
        # 8. Ograniczenie do podanego miasta
        params["by_city"] = city
        print(f"🔍 Wyszukiwanie browarów w mieście: {city}...")
    else:
        print("🌍 Wyszukiwanie 20 pierwszych browarów...")

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Rzuca wyjątek dla kodów 4xx/5xx
        data: List[Dict[str, Any]] = response.json()

        # Tworzenie listy instancji klasy Brewery
        brewery_list = [Brewery(item) for item in data]

        return brewery_list

    except requests.exceptions.RequestException as e:
        print(f"❌ Wystąpił błąd podczas połączenia z API: {e}")
        return []


def main():
    # --- 8. Implementacja modułu argparse ---
    parser = argparse.ArgumentParser(description="Pobiera informacje o browarach z Open Brewery DB API.")
    parser.add_argument(
        '--city',
        type=str,
        help='Opcjonalne: Ogranicza pobierane browary do podanego miasta.',
        default=None
    )
    args = parser.parse_args()

    # Pobieranie danych
    breweries = fetch_breweries(args.city)

    print("\n" + "=" * 40)

    if not breweries:
        print("Nie znaleziono browarów lub wystąpił błąd.")
        return

    print(f"Znaleziono {len(breweries)} browarów.")
    print("--- Lista browarów: ---")

    # 7. Iteracja i wyświetlenie każdego obiektu
    for brewery in breweries:
        # Drukujemy obiekt, a dzięki __str__ jest on automatycznie formatowany
        print(brewery)
        print("-" * 20)


if __name__ == "__main__":
    main()