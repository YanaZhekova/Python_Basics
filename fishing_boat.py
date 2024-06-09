budget = int(input())
season = input()
fishman = int(input())

boat_rent = 0
total_cost = 0.0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer":
    boat_rent = 4200
elif season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishman <= 6:
    total_cost = boat_rent - boat_rent * 0.10
elif 11 >= fishman > 7:
    total_cost = boat_rent - boat_rent * 0.15
elif fishman > 12:
    total_cost = boat_rent - boat_rent * 0.25

if season != "Autumn" and fishman % 2 == 0:
    total_cost = total_cost - total_cost * 0.05

if budget >= total_cost:
    left_money = budget - total_cost
    print(f"Yes! You have {left_money:.2f} leva left.")
elif budget < total_cost:
    need_money = total_cost - budget
    print(f"Not enough money! You need {need_money:.2f} leva.")