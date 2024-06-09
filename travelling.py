destination = input()
min_budget = float(input())

budget = 0.0

while destination != "End":
    save_money = float(input())
    budget += save_money
    if budget >= min_budget:
        print(f"Going to {destination}!")
        budget = 0
        destination = input()
        if destination == "End":
            break
        min_budget = float(input())
