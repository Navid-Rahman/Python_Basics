print("Hello and welcome to python")
print("Hello and welcome to python Functions")


def my_function():
    print("Bro this is my function")


def say_my_name():
    print("Heisenberg")


say_my_name()


def who_are_you(blah):
    print(f"Hello {blah}")


who_are_you("Booo")


def print_color_red():
    color = "red"
    print(color)


color = "blue"
print(color)

print_color_red()


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


print_numbers(highest_number=12, lowest_number=3)


def multiply_numbers(a, b):
    return a * b


print(multiply_numbers(1, 2))

solution = multiply_numbers(12, 45)
print(solution)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return current_tax_rate * cost_of_item


final_cost = buy_item(50)

print(final_cost)
