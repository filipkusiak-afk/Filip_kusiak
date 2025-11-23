# main.py

import requests
import argparse
from typing import List, Optional, Dict, Any

# Adres bazowy API
API_URL = "https://api.openbrewerydb.org/v1/breweries"


## 🍺 Klasa Brewery
# Zgodnie z dokumentacją API i wymaganiem typowania
class Brewery:
    """
    Reprezentuje pojedynczy browar pobrany z Open Brewery DB API.
    """
    # Atrybuty z typowaniem zgodnym z API (wybrano kluczowe pola)
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: Optional[str]
    country: str
    phone: Optional[str]
    website_url: Optional[str]

    # Dodatkowe pola, które można zmapować
    # longitude: Optional[str]
    # latitude: Optional[str]

    def __init__(self, data: Dict[str, Any]):
        """Inicjalizuje obiekt Brewery na podstawie słownika danych z API."""
        self.id = data.get('id', 'N/A')
        self.name = data.get('name', 'N/A')
        self.brewery_type = data.get('brewery_type', 'N/A')
        self.address_1 = data.get('address_1')
        self.city = data.get('city', 'N/A')
        self.state_province = data.get('state_province')
        self.postal_code = data.get('postal_code')
        self.country = data.get('country', 'N/A')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')

    def __str__(self) -> str:
        """
        Magiczna metoda __str__ opisująca dane przechowywane w obiekcie.
        """
        address_line = f"{self.address_1}, " if self.address_1 else ""
        state_zip = (f"{self.state_province} " if self.state_province else "") + \
                    (f"{self.postal_code}" if self.postal_code else "")

        info = [
            f"**ID:** {self.id}",
            f"**Nazwa:** {self.name}",
            f"**Typ:** {self.brewery_type.capitalize()}",
            f"**Lokalizacja:** {address_line}{self.city}, {state_zip}, {self.country}",
        ]

        if self.phone:
            info.append(f"**Telefon:** {self.phone}")
        if self.website_url:
            info.append(f"**WWW:** {self.website_url}")

        # Zwrócenie sformatowanego stringa
        return "\n  ".join(info)


## 🚀 Funkcje Logiki Skryptu

def fetch_breweries(city: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Pobiera dane browarów z API, opcjonalnie filtrując po mieście.
    Limituje do pierwszych 20 wyników.
    """
    params = {'per_page': 20}
    if city:
        # Filtr dla miasta
        params['by_city'] = city.lower()
        print(f"-> Szukam browarów w mieście: **{city}**")
    else:
        print("-> Szukam pierwszych 20 browarów (bez filtrowania po mieście)")

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Wyrzuci wyjątek dla kodów 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"🚨 Błąd połączenia z API lub zapytania: {e}")
        return []


def create_brewery_list(data: List[Dict[str, Any]]) -> List[Brewery]:
    """Tworzy listę instancji klasy Brewery z listy słowników danych."""
    return [Brewery(item) for item in data]


def parse_arguments() -> argparse.Namespace:
    """Konfiguruje i parsuje argumenty wiersza poleceń."""
    parser = argparse.ArgumentParser(
        description="Pobiera dane browarów z Open Brewery DB API."
    )
    # Dodanie opcjonalnego argumentu --city
    parser.add_argument(
        '--city',
        type=str,
        required=False,
        help='Ogranicza pobrane browary do podanego miasta (np. --city=Berlin).'
    )
    return parser.parse_args()


def main():
    """Główna funkcja wykonawcza skryptu."""

    # 8. Wczytywanie parametru city
    args = parse_arguments()
    city_filter = args.city

    # Pobieranie danych z API
    api_data = fetch_breweries(city_filter)

    if not api_data:
        print("\nNie znaleziono browarów lub wystąpił błąd.")
        return

    print(f"Pobrano {len(api_data)} browarów.\n")

    # 7. Tworzenie listy instancji klasy Brewery
    breweries_list = create_brewery_list(api_data)

    # 7. Iteracja i wyświetlanie każdego obiektu
    print("--- 📋 LISTA POBRANYCH BROWARÓW ---")
    for i, brewery in enumerate(breweries_list, 1):
        print(f"\n## Browar #{i}")
        print(brewery)  # Użycie magicznej metody __str__


if __name__ == "__main__":
    main()