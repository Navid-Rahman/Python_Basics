user_input =  int(input("Please enter your marks: "))

if user_input >=90:
    print("A")
elif 80 <= user_input <= 89:
    print("B")
elif 70 <= user_input <= 79:
    print("C")
elif 60 <= user_input <= 69:
    print("D")
elif user_input <=59:
    print("F")