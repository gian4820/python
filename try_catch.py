try:
   #div = 85/0
    number = int(input("Enter a number: "))
    print ("The number you have enter is: ", number)
    
except ValueError as err:
    print ("ERROR, add an integer.")
    print("Error code: ", err)
except ZeroDivisionError as err:
    print ("ERROR: You can't divide by zero")
    print("Error code: ", err)