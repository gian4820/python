data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
#your code goes here
length=len(data)
print ("len=", + length)

min = min(data)
print("min=", + min)

max = max(data)
print ("max=", + max)

print ("Sort array")
data.sort()


total = 0
reduce = (data[1:(length-2)])
print (reduce)

for i in reduce:
    total = total + i
print (total)