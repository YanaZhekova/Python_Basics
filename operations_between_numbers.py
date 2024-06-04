num1 = int(input())
num2 = int(input())
operator = input()
sum = 0

if operator == '+':
    sum = num1 + num2
    if sum % 2 == 0:
        print(f"{num1} + {num2} = {sum} - even")
    else:
        print(f"{num1} + {num2} = {sum} - odd")
elif operator == '-':
    sum = num1 - num2
    if sum % 2 == 0:
        print(f"{num1} - {num2} = {sum} - even")
    else:
        print(f"{num1} - {num2} = {sum} - odd")
elif operator == '*':
    sum = num1 * num2
    if sum % 2 == 0:
        print(f"{num1} * {num2} = {sum} - even")
    else:
        print(f"{num1} * {num2} = {sum} - odd")
elif operator == '/':
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = float(num1 / num2)
        print(f"{num1} / {num2} = {sum:.2f} ")

elif operator == '%':
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 % num2
        print(f"{num1} % {num2} = {sum}")
