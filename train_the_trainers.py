number_of_jury = int(input())
command = input()
total_grade = 0.0
counter_all_presentation = 0
final_grade =0.0
while command != "Finish":
    for i in range(number_of_jury):
        current_grade = float(input())
        total_grade += current_grade
        counter_all_presentation += 1
    average_grade = total_grade / number_of_jury
    print(f"{command} - {average_grade:.2f}.")
    final_grade += total_grade
    total_grade = 0.0
    command = input()

print(f"Student's final assessment is {(final_grade/counter_all_presentation):.2f}." )
