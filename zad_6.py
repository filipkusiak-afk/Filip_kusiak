# zad_6.py
from typing import List, Union


# Używamy Union[int, float] dla elementów, ponieważ potęgowanie może dać float
def process_and_combine_lists(list1: List[Union[int, float]], list2: List[Union[int, float]]) -> List[
    Union[int, float]]:
    """Łączy dwie listy, usuwa duplikaty i podnosi każdy element do potęgi 3."""

    # 1. Złączenie list
    combined_list = list1 + list2

    # 2. Usunięcie duplikatów (konwersja na zbiór 'set' usuwa duplikaty)
    unique_elements = set(combined_list)

    # 3. Podniesienie każdego elementu do potęgi 3
    # Używamy list comprehension do stworzenia nowej listy
    result_list = [x ** 3 for x in unique_elements]

    # 4. Zwrot powstałej listy
    return result_list


# Przykłady użycia
list_a = [1, 2, 3, 2, 5]
list_b = [3, 6, 7, 1]
processed_list = process_and_combine_lists(list_a, list_b)

print(f"Lista A: {list_a}")
print(f"Lista B: {list_b}")
# Unikalne elementy: {1, 2, 3, 5, 6, 7}
# Potęgi: 1^3=1, 2^3=8, 3^3=27, 5^3=125, 6^3=216, 7^3=343
print(f"Wynikowa lista (unikalne elementy do potęgi 3): {processed_list}")

# Wynik:
# Lista A: [1, 2, 3, 2, 5]
# Lista B: [3, 6, 7, 1]
# Wynikowa lista (unikalne elementy do potęgi 3): [1, 8, 27, 216, 125, 343] (kolejność może być inna ze względu na konwersję na set)