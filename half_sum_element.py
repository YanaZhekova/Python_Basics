n = int(input())
sum = 0
diff = 0

find_sum = False
for i in range(1,n+1):
    number = int(input())
    sum += number
    diff -= abs(number)
for i in range(1,n+1):
    print(i)

