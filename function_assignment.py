def user_dictionary(first_name, last_name, age):
    created_user_dictionary = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

    return created_user_dictionary


solution_dictionary = user_dictionary(first_name="John", last_name="Doe",age= 18)
print(solution_dictionary)