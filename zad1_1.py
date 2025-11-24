class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        # Obliczamy sumę ocen
        suma = sum(self.marks)
        # Obliczamy ilość ocen
        ilosc = len(self.marks)

        # Obliczamy średnią
        srednia = suma / ilosc

        if srednia > 50:
            return True
        else:
            return False


# --- Sprawdzenie ---

# Tworzymy obiekt 1 (Jan ma same 60-tki, więc zdał)
student1 = Student("Jan", [60, 60, 60])
wynik1 = student1.is_passed()
print(wynik1)

# Tworzymy obiekt 2 (Anna ma same 30-tki, nie zdała)
student2 = Student("Anna", [30, 30, 30])
wynik2 = student2.is_passed()
print(wynik2)