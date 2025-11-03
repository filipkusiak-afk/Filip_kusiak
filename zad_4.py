def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


if __name__ == "__main__":
    wyswietl_co_drugi(list(range(10)))
