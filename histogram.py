n = int(input())

numbers_under_200 = 0
numbers_between_200_399 = 0
numbers_between_400_599 = 0
numbers_between_600_799 = 0
numbers_over_800 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        numbers_under_200 += 1
    elif 399 >= num >= 200:
        numbers_between_200_399 += 1
    elif 599 >= num >= 400:
        numbers_between_400_599 += 1
    elif 799 >= num >= 600:
        numbers_between_600_799 += 1
    elif num >= 800:
        numbers_over_800 += 1
percentage_under_200 = (numbers_under_200 / n) * 100
percentage_between_200_399 = (numbers_between_200_399 / n) * 100
percentage_between_400_599 = (numbers_between_400_599 / n) * 100
percentage_between_600_799 = (numbers_between_600_799 / n) * 100
percentage_over_800 = (numbers_over_800 / n) * 100

print(f"{percentage_under_200:.2f}%")
print(f"{percentage_between_200_399:.2f}%")
print(f"{percentage_between_400_599:.2f}%")
print(f"{percentage_between_600_799:.2f}%")
print(f"{percentage_over_800:.2f}%")
