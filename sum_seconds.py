first_seconds = int(input())
second_seconds = int(input())
third_seconds = int(input())

time = first_seconds + second_seconds + third_seconds
minutes = time // 60
seconds = time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
