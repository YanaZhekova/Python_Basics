floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i % 2 == 0 and i != floors:
            print(f"O{i}{j} ", end="")
        elif i % 2 != 0 and i != floors:
            print(f"A{i}{j} ", end="")
        elif i == floors:
            print(f"L{i}{j} ", end="")

    print()
