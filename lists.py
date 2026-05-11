"""
Lists are a collection of data
"""

my_list = [40, 34, 12, 78]
print(my_list)
print(my_list[1])
my_list.append(1000)
print(my_list)
my_list.insert(0, 1000)
print(my_list)
my_list.remove(12)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)

peoples_list = ["Navid", "John", "Michael", "David"]
print(peoples_list)
print(peoples_list[0])
print(peoples_list[1])
print(peoples_list[2])
print(len(peoples_list))

# Slicing
print(peoples_list[0:2]) # This means 0 to 2. Not including 2
