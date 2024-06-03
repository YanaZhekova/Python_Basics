year_taxes = int(input())

snickers = year_taxes - year_taxes * 0.4
clothes = snickers - snickers * 0.2
ball = clothes * 0.25
accessories = ball * 0.2

total = snickers + clothes + ball + accessories
print(total + year_taxes )
