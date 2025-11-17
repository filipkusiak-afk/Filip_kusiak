# zad_3.py
def is_even(number: int) -> bool:
    """Sprawdza, czy liczba jest parzysta. Zwraca True/False."""
    # Operator modulo (%) zwraca resztę z dzielenia
    return number % 2 == 0

# Uruchomienie funkcji i zapisanie wyniku
test_number = 17
is_test_number_even = is_even(test_number)

# Wykorzystanie warunku logicznego
if is_test_number_even:
    print(f"Liczba {test_number} jest parzysta")
else:
    print(f"Liczba {test_number} jest nieparzysta")

# Wynik dla 17: Liczba 17 jest nieparzysta
# Wynik dla 24: Liczba 24 jest parzysta