user_dictionary = {
    "username": "john123",
    "name" : "John",
    "age" : 25,
    "city" : "New York",

}
for key, value in user_dictionary.items():
    print(key, value)


user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary)

print(user_dictionary)
print(user_dictionary.get("username"))
print(user_dictionary.get("name"))

user_dictionary["married"] = True
print(user_dictionary)
print(len(user_dictionary))

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

# del user_dictionary

