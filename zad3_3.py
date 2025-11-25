# --- ZADANIE 3: Nieruchomości (Dziedziczenie) ---

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość przy {self.address}: {self.area}m2, {self.rooms} pokoje, cena: {self.price}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        # Wywołanie konstruktora klasy nadrzędnej (Property)
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        # Rozszerzamy opis o wielkość działki
        base_desc = super().__str__()
        return f"[DOM] {base_desc}, Działka: {self.plot}m2"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        # Wywołanie konstruktora klasy nadrzędnej (Property)
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        # Rozszerzamy opis o piętro
        base_desc = super().__str__()
        return f"[MIESZKANIE] {base_desc}, Piętro: {self.floor}"

# Tworzenie obiektów
house1 = House(150, 5, 850000, "Kwiatowa 5", 1000)
flat1 = Flat(50, 2, 450000, "Centrum 10/5", 3)

# Wyświetlanie
print("--- ZADANIE 3: NIERUCHOMOŚCI ---")
print(house1)
print(flat1)