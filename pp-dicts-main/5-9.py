import csv

# ---- 1. WCZYTANIE MAPOWANIA (SŁOWNIK KOD -> NAZWA) ----
provinces = {}

# Otwieramy plik CSV, który działa jak legenda (np. K = Małopolskie).
with open("province.csv", "r", encoding="utf-8") as file:
    # DictReader jest super, bo pozwala odwoływać się do kolumn po nazwach
    # ("Letter", "Name"), a nie po numerach indeksów.
    reader = csv.DictReader(file)
    for row in reader:
        # strip() usuwa zbędne spacje, upper() zamienia na wielkie litery.
        # To tzw. "czyszczenie danych" - ważne, żeby "k" i "K" były traktowane tak samo.
        letter = row["Letter"].strip().upper()
        name = row["Name"].strip()
        
        # Zapisujemy do słownika: klucz 'K' -> wartość 'Małopolskie'
        provinces[letter] = name

# ---- 2. PRZYGOTOWANIE LICZNIKÓW ----
# Tworzymy słownik wyników, np. {'Małopolskie': 0, 'Mazowieckie': 0, ...}
# Każde województwo na start ma 0 pojazdów.
counts = {name: 0 for name in provinces.values()}

# ---- 3. ZLICZANIE POJAZDÓW ----
with open("vehicle.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Wczytujemy rejestrację (np. "KR12345") i czyścimy ją.
        reg = line.strip().upper()
        
        # Puste linie pomijamy
        if not reg:
            continue
            
        # Pobieramy PIERWSZĄ literę rejestracji (np. "K").
        # To ona (według tego kodu) identyfikuje województwo.
        first_letter = reg[0]

        # Sprawdzamy, czy ta litera jest w naszej bazie województw.
        if first_letter in provinces:
            # 1. Tłumaczymy literę na nazwę (K -> Małopolskie)
            province_name = provinces[first_letter]
            # 2. Dodajemy +1 do licznika tego konkretnego województwa
            counts[province_name] += 1
        else:
            # Obsługa błędów - np. rejestracje zagraniczne lub błędne dane
            print("Unknown region letter:", first_letter)

# ---- 4. RAPORT KOŃCOWY ----
print("Vehicles per province")
print("======================")
for province, count in counts.items():
    print(f"{province}: {count}")