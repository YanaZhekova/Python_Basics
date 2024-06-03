deposit_sum = float(input())
period = int(input())
percentage_rate = float(input())


annual_rate = deposit_sum * (percentage_rate / 100)
month_rate = annual_rate / 12

total_sum = float(deposit_sum + period * month_rate)

print(total_sum)