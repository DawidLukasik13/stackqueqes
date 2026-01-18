import json

# Otwieramy plik 'computer.json'.
with open('computer.json', 'r', encoding='utf-8') as file:
    # Wczytujemy dane.
    # W tym przypadku zmienna 'data' to jeden SŁOWNIK (jeden konkretny komputer),
    # a nie lista wielu komputerów.
    data = json.load(file)

# ---- PĘTLA PO CECHACH OBIEKTU ----
# Ponieważ 'data' to słownik, używamy .items(), aby dostać się do par:
# Klucz (np. "procesor") i Wartość (np. "Intel i7").
for key, value in data.items():
    print(key, ":", value)