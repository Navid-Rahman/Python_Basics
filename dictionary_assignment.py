my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 1964,
    "mileage": 8000,
}

for key, value in my_vehicle.items():
    print(key, value)

vehicle2 = my_vehicle.copy()

vehicle2["num_of_tires"] = 4

vehicle2.pop("mileage")

for key in vehicle2.items():
    print(key)