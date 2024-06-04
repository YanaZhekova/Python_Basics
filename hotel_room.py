month = input()
days = int(input())

studio_sum = 0.0
apartment_sum = 0.0
price_studio = 0.0
price_apartment = 0.0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 14 >= days > 7:
        studio_sum = days * price_studio - (days * price_studio * 0.05)
    elif days > 14:
        studio_sum = days * price_studio - (days * price_studio * 0.3)
    else:
        studio_sum = days * price_studio
elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartment = 68.70
    if days > 14:
        studio_sum = days * price_studio - (days * price_studio * 0.2)
    else:
        studio_sum = days * price_studio
else:
    price_studio = 76
    price_apartment = 77
    studio_sum = days * price_studio

if days > 14:
    apartment_sum = days * price_apartment - (days * price_apartment * 0.10)
else:
    apartment_sum = days * price_apartment
print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")
