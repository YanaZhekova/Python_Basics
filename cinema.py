text = input()
row = int(input())
col = int(input())

if text == "Premiere":
    prise = float(row * col * 12)
    print(f"{prise:.2f} leva")
elif text == "Normal":
    prise = float(row * col * 7.5)
    print(f"{prise:.2f} leva")
elif text == "Discount":
    prise = float(row * col * 5)
    print(f"{prise:.2f} leva")
