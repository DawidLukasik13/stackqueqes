import json

def load_data():
    with open("reservations.json", "r", encoding="utf-8") as f:
        return json.load(f)

def count_rooms(data):
    return len(data)

def count_paid(data):
    return sum(1 for r in data if r["paid"])

def count_unpaid(data):
    return sum(1 for r in data if not r["paid"])

def total_paid(data):
    return sum(r["price"] for r in data if r["paid"])

def total_unpaid(data):
    return sum(r["price"] for r in data if not r["paid"])

data = load_data()

print("Number of rooms:", count_rooms(data))
print("Paid reservations:", count_paid(data))
print("Unpaid reservations:", count_unpaid(data))
print("Total paid value:", total_paid(data))
print("Total unpaid value:", total_unpaid(data))
