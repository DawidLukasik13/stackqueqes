import json

# ---- 1. WCZYTANIE DANYCH ----
# Otwieramy plik 'euro.json'. Encoding utf-8 jest ważny, żeby nie "krzaczyło" polskich znaków.
with open("euro.json", "r", encoding="utf-8") as f:
    # json.load(f) zamienia tekst z pliku na słownik Python.
    # Wynik trafia do zmiennej 'data'.
    data = json.load(f)

# ---- 2. WYŚWIETLENIE NAGŁÓWKA ----
# To są po prostu napisy, które tworzą "czapkę" tabeli.
print("Date            Buying Rate     Selling Rate")
print("============================================")

# ---- 3. PĘTLA PO DANYCH ----
# UWAGA: Tutaj struktura JSON jest głębsza.
# Zmienna 'data' to słownik, który ma klucz "rates" (stawki).
# Dopiero pod tym kluczem znajduje się lista, po której możemy iterować.
for entry in data["rates"]:
    
    # ---- 4. FORMATOWANIE WIERSZA ----
    # f"..." to f-string.
    # {entry['bid']:.4f} -> Pobierz cenę kupna i pokaż DOKŁADNIE 4 cyfry po przecinku.
    # To standard w finansach (np. 4.3210 zamiast 4.321).
    print(f"{entry['effectiveDate']}      {entry['bid']:.4f}          {entry['ask']:.4f}")