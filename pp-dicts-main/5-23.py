import json

with open("euro.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Date            Buying Rate     Selling Rate")
print("============================================")

for entry in data["rates"]:
    print(f"{entry['effectiveDate']}      {entry['bid']:.4f}          {entry['ask']:.4f}")
