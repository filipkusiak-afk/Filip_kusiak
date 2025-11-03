def wyswietl_imiona(imiona):
    for imie in imiona:
        print(imie)

wyswietl_imiona(["Anna", "Kasia", "Tomek", "Ola", "Piotr"])


# a) Funkcja, która otrzymuje listę 5 imion i wyświetla każde z nich


def pomnoz_przez_dwa_for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

# funkcja z wykorzystaniem pętli for

def pomnoz_przez_dwa_lista(liczby):
    return [liczba * 2 for liczba in liczby]

# funkcja z wykorzystaniem listy składanej

print(pomnoz_przez_dwa_for([1, 2, 3, 4, 5]))
print(pomnoz_przez_dwa_lista([1, 2, 3, 4, 5]))

# wykorzystanie obu funkcji, dla pętli for i dla listy składanej

def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)

wyswietl_parzyste(list(range(10)))  # liczby 0–9

# funkcja, która otrzyma w parametrze listę 10 liczb i pokaże tylko parzyste.

def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])

wyswietl_co_drugi(list(range(10)))
