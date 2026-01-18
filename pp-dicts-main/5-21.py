import json

# ---- 1. TWORZENIE DANYCH (SŁOWNIK) ----
# Tworzymy słownik, który opisuje jeden konkretny film.
# Zwróć uwagę, że Python miesza różne typy danych:
# - "Interstellar" to String (napis)
# - 2014 to Integer (liczba całkowita)
# - 9.5 to Float (liczba zmiennoprzecinkowa)
favourite = {
    "title": "Interstellar",
    "year": 2014,
    "genre": "Sci-Fi",
    "director": "Christopher Nolan",
    "rating": 9.5
}

# ---- 2. ZAPIS DO PLIKU ----
# "w" (write) - tryb zapisu. Jeśli plik nie istnieje, zostanie stworzony.
# Jeśli istnieje - jego zawartość zostanie wykasowana i nadpisana!
with open("favourite.json", "w", encoding="utf-8") as f:
    # json.dump zamienia słownik Python na format tekstowy JSON.
    # indent=4 sprawia, że plik będzie wyglądał ładnie (z wcięciami),
    # zamiast być jedną długą linijką.
    json.dump(favourite, f, indent=4)

print("Saved to favourite.json")