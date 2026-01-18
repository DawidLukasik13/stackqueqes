countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "Czech Republic", "population": 10700000},
    {"name": "Spain", "population": 47000000},
    {"name": "France", "population": 67000000}
]

print("COUNTRY | POPULATION")
for c in countries:
    print(c["name"], '|', c["population"])
