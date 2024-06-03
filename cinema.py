text = input()
row = int(input())
col = int(input())

if text == "Premiere":
    price = float(row * col * 12)
    print(f"{price:.2f} leva")
elif text == "Normal":
    price = float(row * col * 7.5)
    print(f"{price:.2f} leva")
elif text == "Discount":
    price = float(row * col * 5)
    print(f"{price:.2f} leva")
