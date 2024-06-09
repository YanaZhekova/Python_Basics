group = int(input())

all_people = 0
people_musala = 0
people_montBlanc = 0
people_kilimanjaro = 0
people_k2 = 0
people_everest = 0

for i in range(group):
    people_in_group = int(input())
    all_people += people_in_group
    if people_in_group <= 5:
        people_musala += people_in_group
    elif 12 >= people_in_group >= 6:
        people_montBlanc += people_in_group
    elif 25 >= people_in_group >= 13:
        people_kilimanjaro += people_in_group
    elif 40 >= people_in_group >= 26:
        people_k2 += people_in_group
    elif people_in_group >= 41:
        people_everest += people_in_group

percentage_musala = (people_musala/all_people) * 100
percentage_montBlanc = (people_montBlanc/all_people) * 100
percentage_kilimanjaro = (people_kilimanjaro/all_people) * 100
percentage_k2 = (people_k2/all_people) * 100
percentage_everest = (people_everest/all_people) * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_montBlanc:.2f}%')
print(f'{percentage_kilimanjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')