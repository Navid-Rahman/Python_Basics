"""
String Formatting
"""

first_name = "Navid"
last_name =  "Rahman"

print("Hi" + first_name)
print(f"Hi {first_name}")

sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))