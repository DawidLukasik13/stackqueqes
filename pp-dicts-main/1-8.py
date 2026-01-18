price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("PRICES BEFORE DISCOUNT")
total_before = 0
for item, price in price_list.items():
    print(item, price)
    total_before += price

print("Total before:", total_before)

# Apply 10% discount
for item in price_list:
    price_list[item] = round(price_list[item] * 0.90, 2)

print("\nPRICES AFTER 10% DISCOUNT")
total_after = 0
for item, price in price_list.items():
    print(item, price)
    total_after += price

print(f"Total after: {total_after:.2f}")