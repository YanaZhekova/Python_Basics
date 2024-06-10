first_number = int(input())
second_number = int(input())
sum1 = 0
sum2 = 0
for i in range(first_number, second_number + 1):
    number1 = str(i)
    for j in range(0, len(number1), +2):
        sum1 += int(number1[j])

    for k in range(1, len(number1), +2):
        sum2 += int(number1[k])
    if sum1 == sum2:
        print(i, end=" ")
    else:
        sum1=0
        sum2=0
