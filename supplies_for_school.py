pens = int(input())
markers = int(input())
litres = int(input())
percentage_discount = int(input())

sum_pens = pens * 5.80
sum_markers = markers * 7.20
sum_litres = litres * 1.20
discount =float( (sum_pens + sum_markers + sum_litres)* (percentage_discount/100))
total_sum = sum_pens + sum_markers + sum_litres

print (total_sum-discount)