flowers = input()
count = int(input())
budget = int(input())

price = 0
total_price = 0.0

if flowers == 'Roses':
    price = 5
    if count >= 80:
        total_price += (price * count - (price * count * 0.1))
    else:
        total_price = price * count
elif flowers == 'Dahlias':
    price = 3.80
    if count >= 90:
        total_price += (price * count - (price * count * 0.15))
    else:
        total_price = price * count
elif flowers == 'Tulips':
    price = 2.80
    if count >= 80:
        total_price += (price * count - (price * count * 0.15))
    else:
        total_price = price * count
elif flowers == 'Narcissus':
    price = 3
    if count <= 120:
        total_price += (price * count + (price * count * 0.15))
    else:
        total_price = price * count
elif flowers == 'Gladiolus':
    price = 2.5
    if count <= 80:
        total_price += (price * count + (price * count * 0.20))
    else:
        total_price = price * count

if budget >= total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {count} {flowers} and {money_left:.2f} leva left.")
elif budget < total_price:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
