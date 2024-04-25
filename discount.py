cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for x in cart:
    total = total + x
print (total)
total = total*discount/100
print (total)
