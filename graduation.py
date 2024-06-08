name = input()

total_grade = 0.0
fail_grade = 0
counter = 1

while counter <= 12:
    grade = float(input())
    total_grade += grade
    if grade < 4:
        fail_grade += 1
        break
    # if fail_grade > 1:
    #     break
    counter += 1

if fail_grade >= 1:
    print(f"{name} has been excluded at {counter} grade")
else:
    average_grade = total_grade / (counter-1)
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
