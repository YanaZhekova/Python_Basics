command = input()
total_balance = 0
while command != "NoMoreMoney":
    current_number = float(command)
    if current_number < 0:
        print("Invalid operation!")
        break
    total_balance += current_number
    print(f"Increase: {current_number:.2f}")
    command = input()
print(f"Total: {total_balance:.2f}")