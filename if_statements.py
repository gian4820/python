name = input ('What is your name? ')
years_old = input ('How old are you? ')
gender = input ('Gender? M or F? ')

print ("######################")

print("Hello " + name)

if years_old > '17':
    print("You are an adult")
else:
    print("You are a kid")

if (gender == 'M'):
    print ("You are a Male")
elif (gender == 'F'):
    print ("You are Female")
else:
    print ("Error, invalid!")




