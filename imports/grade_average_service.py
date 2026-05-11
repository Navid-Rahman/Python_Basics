def calculate_homework(homework_assignments_args):
    sum_of_grades = 0
    for homework in homework_assignments_args.values():
        sum_of_grades += homework

    final_grade = round(sum_of_grades/ len(homework_assignments_args))
    print(final_grade)
