def two_arguments_bigger_than_third (a:int, b: int, c: int) -> bool:
    "sprawdza czy suma a i b jest większa od c"
    return (a+b) >=c

"Przykłady użycia"
print(f"3 + 5 >= 7? {two_arguments_bigger_than_third(3, 5, 7)}") #True
print(f"2 + 4 >= 7? {two_arguments_bigger_than_third(2,4,7)}") #False

