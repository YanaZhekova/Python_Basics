lily_years = int(input())
price_washing_machine = float(input())
price_toy = float(input())

spend_money = 0.0
count_toys=0
money_even_birthday =9

for i in range(1,lily_years+1):
    if i % 2 == 0:
        spend_money += money_even_birthday
        money_even_birthday += 10
    else:
        count_toys += 1


spend_money = spend_money + count_toys * price_toy

if spend_money >= price_washing_machine:
    print(f"Yes! {(spend_money-price_washing_machine):.2f}")
else:
    print(f"No! {abs(spend_money-price_washing_machine):.2f}")
