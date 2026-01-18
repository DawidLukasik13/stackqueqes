import json

# Tworzymy pusty słownik, który będziemy wypełniać danymi.
product = {}

# ---- 1. POBIERANIE DANYCH ----
product["name"] = input("Product name: ")

# float(...) jest konieczny! Funkcja input() zawsze zwraca tekst (napis).
# Bez rzutowania na float, w JSON cena zapisałaby się jako "19.99" (tekst),
# a my chcemy 19.99 (liczbę), żeby móc potem na niej liczyć.
product["price"] = float(input("Price: "))

# .lower() zamienia wszystko na małe litery.
# Dzięki temu zadziała wpisanie "Yes", "YES", "yes" czy "YeS".
paid_input = input("Paid? (yes/no): ").lower()

# ---- 2. OPERATOR TRÓJARGUMENTOWY (Ternary Operator) ----
# To skrócony zapis instrukcji warunkowej "if".
# Czytamy to tak:
# Wstaw True JEŚLI wpisano "yes", W PRZECIWNYM RAZIE wstaw False.
product["paid"] = True if paid_input == "yes" else False

# ---- 3. ZAPIS DO PLIKU ----
# Otwieramy plik w trybie zapisu ("w").
with open("product.json", "w", encoding="utf-8") as f:
    # json.dump automatycznie przetłumaczy typy danych:
    # Python True  -> JSON true (małą literą)
    # Python False -> JSON false
    json.dump(product, f, indent=4)

print("Saved to product.json")