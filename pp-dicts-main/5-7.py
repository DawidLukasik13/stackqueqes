# ---- 1. DANE (LISTA SŁOWNIKÓW) ----
# Każdy element listy to osobny słownik reprezentujący jeden hotel.
hotels_in_Krakow = [
    {"name":"Sky", "price":320.00},
    {"name":"Metropol", "price":480.00},
    {"name":"New Port", "price":420.00},
    {"name":"Aparthotel", "price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus", "price":510.00},
    {"name":"Aqua", "price":345.00},
    {"name":"La Boutique", "price":390.00},
    {"name":"Marina", "price":410.00}
]

# ---- 2. FUNKCJA FORMATUJĄCA TEKST ----
def hotel_list(hotels):
    # To jest tzw. "List Comprehension" (wyrażenie listowe) wewnątrz funkcji join.
    # Krok 1: (h["name"] for h in hotels) -> Tworzy listę samych nazw: ["Sky", "Metropol", ...]
    # Krok 2: ", ".join(...) -> Skleja te nazwy w jeden napis, oddzielając je przecinkiem.
    return ", ".join(h["name"] for h in hotels)

# ---- 3. FUNKCJA OBLICZAJĄCA ŚREDNIĄ ----
def avg_price(hotels):
    # Krok 1: sum(...) -> Sumuje ceny wszystkich hoteli.
    # Krok 2: len(hotels) -> Sprawdza, ile jest hoteli na liście.
    # Krok 3: Dzielenie -> Oblicza średnią.
    # Krok 4: round(...) -> Zaokrągla wynik do pełnej liczby całkowitej (bez groszy).
    return round(sum(h["price"] for h in hotels) / len(hotels))

# ---- 4. WYŚWIETLANIE DANYCH ----
# Wywołujemy nasze funkcje dla Krakowa...
print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_price(hotels_in_Krakow))

# ...i dla Sopotu.
print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_price(hotels_in_Sopot))

# ---- 5. LOGIKA PORÓWNANIA ----
# Porównujemy wyniki zwrócone przez funkcję avg_price.
if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    print("Cheaper hotels in: Krakow")
else:
    print("Cheaper hotels in: Sopot")