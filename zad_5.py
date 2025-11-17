# zad_5.py
from typing import List

def contains_value(data_list: List[int], value: int) -> bool:
    """Sprawdza, czy lista zawiera podaną wartość. Zwraca True/False."""
    return value in data_list

# Przykłady użycia
my_list = [10, 20, 30, 40]
print(f"Czy lista {my_list} zawiera 30? {contains_value(my_list, 30)}")   # True
print(f"Czy lista {my_list} zawiera 50? {contains_value(my_list, 50)}")   # False

# Wynik:
# Czy lista [10, 20, 30, 40] zawiera 30? True
# Czy lista [10, 20, 30, 40] zawiera 50? False