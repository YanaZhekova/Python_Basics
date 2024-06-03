price_excursion = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + minions + trucks + teddy_bears

profit = float(puzzles * 2.60) + float(dolls * 3) + float(teddy_bears * 4.10) + float(minions * 8.20) + float(
    trucks * 2)

if total_toys >= 50:
    discount = profit * 0.25
    profit = profit - discount

rent = profit * 0.1

total_profit = profit - rent

if total_profit >= price_excursion:
    left_moneys = total_profit - price_excursion
    print(f"Yes! {left_moneys:.2f} lv left.")
elif total_profit < price_excursion:
    needed_money = price_excursion - total_profit
    print(f"Not enough money! {needed_money:.2f} lv needed.")
