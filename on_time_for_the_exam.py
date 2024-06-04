import math

hour_exam = int(input())
minutes_exam = int(input())
hours_arrived = int(input())
minutes_arrived = int(input())
new_minutes = 0
new_hours = 0

if hours_arrived > hour_exam:
    print("Late")
    if hours_arrived > hour_exam:
        if minutes_arrived >= minutes_exam:
            if minutes_arrived - minutes_exam < 10:
                print(f"{hours_arrived - hour_exam}:0{minutes_arrived - minutes_exam} hours after the start")
            else:
                print(f"{hours_arrived - hour_exam}:{minutes_arrived - minutes_exam} hours after the start")
        else:
            if (minutes_exam + minutes_arrived) <= 59:
                print(f"{minutes_exam + minutes_arrived} minutes after the start")
            else:
                print(f"{hours_arrived - hour_exam}:{minutes_arrived - minutes_exam} hours after the start")

elif hours_arrived == hour_exam and minutes_arrived > minutes_exam:
    print("Late")
    print(f"{minutes_arrived - minutes_exam} minutes after the start")
elif hours_arrived == hour_exam and minutes_arrived <= minutes_exam:
    print("On time")
    print(f"{minutes_exam - minutes_arrived} minutes before the start")

elif hours_arrived < hour_exam:
    if minutes_exam - 30 < 0:
        new_minutes = math.fabs(minutes_exam - 30)
        new_hours = hour_exam - 1
    else:
        new_minutes = minutes_exam - 30
        new_hours = hour_exam
    if new_hours == hours_arrived and new_minutes <= minutes_arrived:
        print("On time")
        print(f"{60 - minutes_arrived} minutes before the start")
    else:
        print("Early")
        print(f"{hours_arrived - hour_exam}: {minutes_arrived - minutes_exam} hours before the start")
