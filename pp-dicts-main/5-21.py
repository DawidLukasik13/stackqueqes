import json

favourite = {
    "title": "Interstellar",
    "year": 2014,
    "genre": "Sci-Fi",
    "director": "Christopher Nolan",
    "rating": 9.5
}

with open("favourite.json", "w", encoding="utf-8") as f:
    json.dump(favourite, f, indent=4)

print("Saved to favourite.json")
