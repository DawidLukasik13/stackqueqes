import csv

# ---- 1. Load province → letter mapping ----
provinces = {}

with open("province.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        letter = row["Letter"].strip().upper()
        name = row["Name"].strip()
        provinces[letter] = name

# ---- 2. Prepare counting dictionary ----
counts = {name: 0 for name in provinces.values()}

# ---- 3. Read vehicles and count by first letter ----
with open("vehicle.txt", "r", encoding="utf-8") as file:
    for line in file:
        reg = line.strip().upper()
        if not reg:
            continue
        first_letter = reg[0]

        if first_letter in provinces:
            province_name = provinces[first_letter]
            counts[province_name] += 1
        else:
            print("Unknown region letter:", first_letter)

# ---- 4. Print results ----
print("Vehicles per province")
print("======================")
for province, count in counts.items():
    print(f"{province}: {count}")
