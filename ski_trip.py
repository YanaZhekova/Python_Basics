days = int(input())
room = input()
rating = input()

price_apartment = 0.0
price_president_apartment = 0.0
price_one_person = 0.0

total_price=0.0

if room == "room for one person":
    price_one_person = 18
    total_price = price_one_person * (days - 1)
    if rating == "positive":
        total_price = total_price + total_price * 0.25
    else:
        total_price = total_price - total_price * 0.1
elif room == "apartment":
    price_apartment = 25
    total_price = price_apartment * (days - 1)
    if days < 10:
        total_price = total_price - total_price * 0.3
    elif 15 >= days >= 10:
        total_price = total_price - total_price * 0.35
    elif days > 15:
        total_price = total_price - total_price * 0.50
    if rating == "positive":
        total_price = total_price + total_price * 0.25
    else:
        total_price = total_price - total_price * 0.1
elif room == "president apartment":
    price_president_apartment = 35
    total_price = price_president_apartment * (days - 1)
    if days < 10:
        total_price = total_price -total_price * 0.1
    elif 15 >= days >= 10:
        total_price = total_price - total_price * 0.15
    elif days > 15:
        total_price = total_price - total_price * 0.20
    if rating == "positive":
        total_price = total_price + total_price * 0.25
    else:
        total_price = total_price - total_price * 0.1

print(f"{total_price:.2f}")
