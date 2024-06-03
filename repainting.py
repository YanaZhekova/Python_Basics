nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

sum_nylon = float((nylon + 2) * 1.5)
sum_paint = float((paint + paint*0.10) * 14.5)
sum_thinner = thinner * 5
sum_bags = 0.4


total_sum = sum_nylon + sum_paint + sum_thinner + sum_bags
sum_craftsman = total_sum * 0.3
print(sum_craftsman*hours + total_sum)