
chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

all_menus = float(chicken_menu * 10.35 + fish_menu * 12.4 + vegetarian_menu * 8.15)

desert = all_menus * 0.2

print(round(all_menus, 2) + desert + 2.5)

