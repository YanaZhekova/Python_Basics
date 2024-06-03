import  math
name_of_movie = input()
time_per_episode = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break /8
time_for_relax = lunch_break / 4
left_time = lunch_break - time_for_lunch - time_for_relax

if time_per_episode <= left_time:
    time = left_time - time_per_episode
    print(f"You have enough time to watch {name_of_movie} and left with {math.ceil(time)} minutes free time.")
elif time_per_episode > left_time:
    needed_time = time_per_episode - left_time
    print(f"You don't have enough time to watch {name_of_movie}, you need {math.ceil(needed_time)} more minutes.")