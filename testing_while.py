total = 0
#your code goes here
passengers = 5
ticket = 100

while passengers > 0:
    age = input()
    age = int(age)

    if age > 3:
        total = total + 100

    passengers = passengers - 1
print (total)