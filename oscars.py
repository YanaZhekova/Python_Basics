actor = input()
point = float(input())
count_jury = int(input())

total_points = point

for i in range(count_jury):
    name_jury = input()
    point_current_jury = float(input())
    current_points = (len(name_jury)*point_current_jury)/2
    total_points += current_points

    if total_points >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points < 1250.5:
    print(f"Sorry, {actor} you need {(1250.5-total_points):.1f} more!")
