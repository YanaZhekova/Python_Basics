budget = float(input())
video_cards = int(input())
gpu = int(input())
ram = int(input())

prise_video_cards = video_cards * 250
prise_gpu = (prise_video_cards * 0.35) * gpu
prise_ram = (prise_video_cards * 0.10) * ram

total_prise = prise_video_cards + prise_gpu + prise_ram

if video_cards > gpu:
    total_prise = total_prise - total_prise * 0.15

if total_prise <= budget:
    left_money = budget - total_prise
    print(f"You have {left_money:.2f} leva left!")
elif total_prise > budget:
    needed_money = total_prise - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
