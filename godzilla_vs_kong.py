budget = float(input())
statists = int(input())
price_clothes = float(input())

total_clothes = statists * price_clothes

if statists >= 150:
    discount = total_clothes * 0.10
    total_clothes = total_clothes - discount

decor = budget * 0.10

total_money = total_clothes + decor

if budget < total_money:
    needed_money = total_money - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
elif budget >= total_money:
    left_money = budget - total_money
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
