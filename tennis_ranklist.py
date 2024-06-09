import math
tournaments = int(input())
first_score = int(input())
total_score = first_score
wins = 0

for tournament in range(1, tournaments + 1):
    stage_tournament = input()

    if stage_tournament == "F":
        total_score += 1200
    elif stage_tournament == "W":
        wins += 1
        total_score += 2000
    elif stage_tournament == "SF":
        total_score += 720

average_tournament = (total_score-first_score) / tournaments

average_wins = (wins / tournaments) * 100

print(f"Final points: {total_score}")
print(f"Average points: {math.floor(average_tournament)}")
print(f"{average_wins:.2f}%")
