import json

with open("dogs.json", "r", encoding="utf-8") as f:
    dogs = json.load(f)

for dog in dogs:
    if dog["age"] < 5:
        print(dog)
