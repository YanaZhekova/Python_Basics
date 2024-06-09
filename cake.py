width = int(input())
length = int(input())
command = input()

area = width * length

while command != "STOP":
    pieces = int(command)
    area -= pieces
    if area <=0:
        break
    command = input()
if area > 0:
    print(f"{area} pieces are left.")
else:
    print(f"No more cake left! You need {abs(area)} pieces more.")