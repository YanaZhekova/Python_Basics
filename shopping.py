budget = float(input())
video_cards = int(input())
gpu = int(input())
ram = int(input())

price_video_cards = video_cards * 250
price_gpu = (price_video_cards * 0.35) * gpu
price_ram = (price_video_cards * 0.10) * ram

total_price = price_video_cards + price_gpu + price_ram

if video_cards > gpu:
    total_price = total_price - total_price * 0.15

if total_price <= budget:
    left_money = budget - total_price
    print(f"You have {left_money:.2f} leva left!")
elif total_price > budget:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
