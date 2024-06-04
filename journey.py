budget = float(input())
season = input()

total_cost = 0.0
place = ""
destination=""

if budget <=100:
    destination = "Bulgaria"
    if season == "summer":
        total_cost = budget*0.3
    elif season == "winter":
        total_cost = budget*0.7
elif budget <=1000:
    destination = "Balkans"
    if season == "summer":
        total_cost = budget * 0.4
    elif season == "winter":
        total_cost = budget * 0.8
elif budget >1000:
    destination = "Europe"
    total_cost = budget * 0.9

if destination == "Europe":
    place = "Hotel"
else:
    if season == "summer":
        place = "Camp"
    elif season == "winter":
        place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {total_cost:.2f}")