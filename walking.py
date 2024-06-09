command = input()

total_steps = 0

while total_steps < 10000:
    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

    current_steps = int(command)

    total_steps += current_steps

    if total_steps >= 10000:
        break

    command = input()

if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")
