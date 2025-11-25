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

# 1. Klasa Library
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka ({self.city}, {self.street}, tel: {self.phone})"


# 2. Klasa Employee
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name} (zatr.: {self.hire_date})"


# 3. Klasa Book
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library  # Obiekt klasy Library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"'{self.author_name} {self.author_surname}' ({self.publication_date}) - {self.number_of_pages} stron [Lokalizacja: {self.library.city}]"


# 4. Klasa Order
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee  # Obiekt klasy Employee
        self.student = student    # Obiekt klasy Student (z zadania 1)
        self.books = books        # Lista obiektów klasy Book
        self.order_date = order_date

    def __str__(self):
        # Tworzymy ładny spis książek w zamówieniu
        books_description = "\n\t- ".join([str(book) for book in self.books])
        return (
            f"ZAMÓWIENIE z dnia {self.order_date}:\n"
            f"  Obsługa: {self.employee}\n"
            f"  Zamawiający: {self.student.name}\n"
            f"  Książki:\n\t- {books_description}"
        )


# --- Tworzenie instancji (Obiekty) ---

# 2 Biblioteki
lib1 = Library("Warszawa", "Koszykowa 1", "00-001", "8:00-20:00", "123-456-789")
lib2 = Library("Kraków", "Rajska 1", "31-000", "9:00-17:00", "987-654-321")

# 3 Pracowników
emp1 = Employee("Adam", "Mickiewicz", "2020-01-01", "1980-05-05", "Warszawa", "Wilcza", "00-002", "111-222-333")
emp2 = Employee("Juliusz", "Słowacki", "2021-06-01", "1990-07-07", "Kraków", "Długa", "31-002", "444-555-666")
emp3 = Employee("Cyprian", "Norwid", "2022-03-15", "1985-12-12", "Gdańsk", "Morska", "80-001", "777-888-999")

# 3 Studentów (wykorzystujemy klasę z Zadania 1)
s1 = Student("Tomek", [45, 50])
s2 = Student("Kasia", [90, 80])
s3 = Student("Marek", [55, 55])

# 5 Książek
# Przypisujemy książki do konkretnych bibliotek (obiektów lib1 i lib2)
b1 = Book(lib1, "2001", "J.K.", "Rowling", 300)
b2 = Book(lib1, "1954", "J.R.R.", "Tolkien", 500)
b3 = Book(lib2, "1965", "Frank", "Herbert", 600)
b4 = Book(lib2, "1986", "Stephen", "King", 1000)
b5 = Book(lib1, "1925", "F.", "Fitzgerald", 200)

# 2 Zamówienia
# Zamówienie 1: Pracownik 1, Student 1, Książki b1 i b2
order1 = Order(emp1, s1, [b1, b2], "2023-10-27")

# Zamówienie 2: Pracownik 2, Student 2, Książki b3, b4, b5
order2 = Order(emp2, s2, [b3, b4, b5], "2023-10-28")

# --- Wyświetlenie zamówień ---
print("-" * 30)
print(order1)
print("-" * 30)
print(order2)
print("-" * 30)