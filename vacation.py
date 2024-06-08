money_needed_for_vacation = float(input())
existing_money = float(input())
count_spend = 0
counter_days = 0

spend_too_much_money = False

while existing_money < money_needed_for_vacation:
    counter_days += 1
    command = input()
    current_money = float(input())

    if command == "spend":
        count_spend += 1
        existing_money -= current_money
        if existing_money <= 0:
            existing_money = 0
    else:
        count_spend = 0
        existing_money += current_money
    if count_spend == 5:
        spend_too_much_money = True
        break

if spend_too_much_money:
    print("You can't save the money.")
    print(f"{counter_days}")
else:
    print(f"You saved the money for {counter_days} days.")
