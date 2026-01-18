price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("PRICES BEFORE DISCOUNT")
total_before = 0
# 1. Pętla .items(): Pobieramy parę (Klucz, Wartość) jednocześnie.
for item, price in price_list.items():
    print(item, price)
    total_before += price  # Szybkie dodawanie do sumy (to samo co: total = total + price)

print("Total before:", total_before)

# Apply 10% discount
# 2. Modyfikacja słownika: Chodzimy po kluczach, żeby zmienić wartości.
for item in price_list:
    # Cena * 0.90 to obniżka o 10%.
    # round(..., 2) zaokrągla wynik do 2 miejsc po przecinku (grosze).
    price_list[item] = round(price_list[item] * 0.90, 2)

print("\nPRICES AFTER 10% DISCOUNT")
total_after = 0
for item, price in price_list.items():
    print(item, price)
    total_after += price

# 3. Formatowanie wyniku:
# :.2f sprawia, że nawet jak wynik to 200.5, wyświetli się ładne "200.50".
print(f"Total after: {total_after:.2f}")