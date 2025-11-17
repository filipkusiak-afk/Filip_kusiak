# zad_1.py
def create_greeting(name: str, surname: str) -> str:
    """Zwraca powitalny string w formacie 'Cześć {name} {surname}!'"""
    return f"Cześć {name} {surname}!"

# Uruchomienie funkcji, zapisanie wyniku i wyświetlenie
result = create_greeting("Anna", "Kowalska")
print(result)

# Wynik: Cześć Anna Kowalska!