print ("FIND THE SECRET CAR FACTORY")
secret = "bmw"
i=1
key = input ("Car factory?")
while secret != key :
    print ("Key Wrong!")
    print (i)
    i = (i + 1)
    key = input ("Car factory?")

print ("Congratulations! the key was " + key)
print ((i - 1), " times fail")