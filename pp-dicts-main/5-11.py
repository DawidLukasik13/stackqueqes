import json
import os

# Nazwa pliku, w którym przechowujemy bazę danych głosów
FILENAME = "voting.json"

# ---- 1. WCZYTYWANIE DANYCH (PAMIĘĆ PROGRAMU) ----
# Sprawdzamy, czy plik z danymi już istnieje na dysku
if os.path.exists(FILENAME):
    # Jeśli plik istnieje, otwieramy go w trybie odczytu ("r" - read)
    with open(FILENAME, "r", encoding="utf-8") as f:
        # Wczytujemy treść JSON i zamieniamy ją na słownik Pythona (np. {"Anna": 2, "Jan": 5})
        votes = json.load(f)
else:
    # Jeśli plik nie istnieje (pierwsze uruchomienie), tworzymy pusty słownik
    votes = {}

# ---- 2. INTERAKCJA Z UŻYTKOWNIKIEM ----
# Pobieramy od użytkownika nazwę kandydata
person_name = input("Name of the person you are voting for: ")

# ---- 3. LOGIKA ZLICZANIA ----
# Aktualizujemy słownik.
# votes.get(person_name, 0) robi dwie rzeczy:
# a) szuka osoby w słowniku i pobiera jej obecny wynik
# b) jeśli osoby nie ma, zwraca wartość domyślną 0
# Na końcu dodajemy +1 do wyniku.
votes[person_name] = votes.get(person_name, 0) + 1

# ---- 4. ZAPISYWANIE DANYCH ----
# Otwieramy plik w trybie zapisu ("w" - write).
# UWAGA: Tryb 'w' kasuje starą zawartość pliku i zastępuje ją nową!
with open(FILENAME, "w", encoding="utf-8") as f:
    # Zapisujemy zaktualizowany słownik 'votes' z powrotem do pliku.
    # indent=4 sprawia, że plik JSON będzie ładnie sformatowany (czytelny dla człowieka).
    json.dump(votes, f, indent=4)

# Potwierdzenie dla użytkownika
print("Vote saved!")