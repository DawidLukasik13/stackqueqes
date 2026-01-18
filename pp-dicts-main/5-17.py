import json

# Otwieramy plik w trybie odczytu ('r').
# Encoding utf-8 zapewnia, że polskie znaki (ą, ę) wyświetlą się poprawnie.
with open('cities.json', 'r', encoding='utf-8') as file:
    # Wczytujemy zawartość.
    # Zakładamy, że w pliku jest LISTA słowników (np. [{"name": "Kraków"}, {"name": "Warszawa"}]).
    data = json.load(file)

# ---- 1. PĘTLA ZEWNĘTRZNA (Idziemy przez listę miast) ----
# Zmienna 'city' w każdym obiegu pętli to jeden pełny słownik (jeden obiekt miasta).
for city in data:
    
    # ---- 2. PĘTLA WEWNĘTRZNA (Idziemy przez szczegóły konkretnego miasta) ----
    # Metoda .items() rozbija słownik na pary: Klucz (np. "country") i Wartość (np. "Poland").
    # Dzięki temu wypisujemy WSZYSTKIE informacje o mieście, linijka po linijce.
    for key, value in city.items():
        print(key, ":", value)
    
    # Pusta linia (print pusty), żeby oddzielić jedno miasto od drugiego w wynikach.
    print()