my_list = [1,2,3,4,5,6,7,8,9,10]

for number in my_list:
    print(number)


sum_of_for_loop = 0
for number in my_list:
    sum_of_for_loop += number

print(sum_of_for_loop)



days_of_the_week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thur", "Fri"]
for day in days_of_the_week:
    print(f"Happy {day}!")


i = 0
while i<5:
    i+=1
    if i ==3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")
