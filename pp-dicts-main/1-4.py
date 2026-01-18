person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Displays name
print("Name:", person["name"])

# Displays hobby
print("Hobby:", person["hobby"])

# Displays entire dictionary
print(person)

# Change surname
person["surname"] = "Nowak"

# Change marriage status
person["married"] = False

# Add gender
person["gender"] = "male"

# Add new hobby
person["hobby"].append("bicycle")

# Add work phone
person["phone"]["work"] = "313131444"

# Display full dictionary again
for key, value in person.items():
    print(f"{key}: {value}")
