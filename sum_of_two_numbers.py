start = int(input())
end = int(input())
magic_number = int(input())
count = 0
right_combination = 0
foundMagicNumber = False
first_number = 0
second_number = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1
        sum = i + j
        if sum == magic_number:
            first_number = i
            second_number = j
            foundMagicNumber = True
            right_combination = count
            break
    if foundMagicNumber:
        break

if foundMagicNumber:
    print(f"Combination N:{right_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{count} combinations - neither equals {magic_number}")