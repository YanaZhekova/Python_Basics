score = int(input())

bonus = 0
if score <= 100:
    bonus += 5
elif 1000 >= score > 100:
    bonus += score * 0.2
elif score > 1000:
    bonus = score * 0.1

if score % 2 == 0:
    bonus += 1
elif score % 5 == 0:
    bonus += 2

print(bonus)
print(float(score) + bonus)
