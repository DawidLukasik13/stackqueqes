import json

product = {}

product["name"] = input("Product name: ")
product["price"] = float(input("Price: "))
paid_input = input("Paid? (yes/no): ").lower()

product["paid"] = True if paid_input == "yes" else False

with open("product.json", "w", encoding="utf-8") as f:
    json.dump(product, f, indent=4)

print("Saved to product.json")
