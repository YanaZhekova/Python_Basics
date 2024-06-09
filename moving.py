width = int(input())
length = int(input())
height = int(input())

area = width * height * length

command = input()

while command != "Done":
    boxes = int(command)
    area -= boxes
    if area < 0:
        break
    command = input()
if area < 0:
    print(f"No more free space! You need {abs(area)} Cubic meters more.")
else:
    print(f"{area} Cubic meters left.")
