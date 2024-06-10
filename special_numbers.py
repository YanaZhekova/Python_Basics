special_number = int(input())
isSpecial = False
print_number = 0
for number in range(1111, 10000):
    current_number = str(number)
    for num in range(0, len(current_number), +1):
        digit = current_number[num]
        if int(digit) !=0 and special_number % int(digit) == 0 :
            isSpecial = True
        else:
            isSpecial = False
            break
    if isSpecial:
        print_number = int(current_number)
        print(f"{print_number}", end=" ")
    else:
        continue
