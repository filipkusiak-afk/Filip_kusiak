def pomnoz_przez_dwa_for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


if __name__ == "__main__":
    print(pomnoz_przez_dwa_for([1, 2, 3, 4, 5]))




def pomnoz_przez_dwa_lista(liczby):
    return [liczba * 2 for liczba in liczby]


if __name__ == "__main__":
    print(pomnoz_przez_dwa_lista([1, 2, 3, 4, 5]))
