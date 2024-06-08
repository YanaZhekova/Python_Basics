number_of_bad_grade = int(input())
command = input()

total_grade = 0.0
last_task = ""
number_of_tasks = 0
counter_fail = 0

isFail = False

while command != "Enough":
    name_task = command
    current_grade = float(input())

    if current_grade <= 4:
        counter_fail += 1

    if counter_fail == number_of_bad_grade:
        isFail = True
        break

    total_grade += current_grade
    last_task = name_task
    number_of_tasks += 1
    command = input()


if isFail:
    print(f"You need a break, {number_of_bad_grade} poor grades.")
else:
    print(f"Average score: {total_grade/number_of_tasks:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {last_task}")