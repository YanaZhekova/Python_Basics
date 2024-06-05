group = int(input())

all_people=0
people_musala = 0
people_montBlanc = 0
people_kilimanjaro= 0
people_k2 = 0
people_everest = 0


for i in range(group):
    people_in_group = int(input())
    all_people += people_in_group
    if people_in_group >=5:
        print(people_in_group)

