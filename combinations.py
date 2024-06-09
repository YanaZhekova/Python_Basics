number = int(input())
counter = 0

for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            sum = i + j + k
            if sum == number:
                counter += 1
print(counter)