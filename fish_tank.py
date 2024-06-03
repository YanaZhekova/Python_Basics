width = int(input())
length = int(input())
height = int(input())
percentage = float(input())

size = width * length * height
litres = float(size * 0.001)
needed_litres = litres * (1- (percentage/100))
print(needed_litres)
