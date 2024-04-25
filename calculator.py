from math import *

print("###############")
print("#-CALCULATOR-#")
print("###############")
print("")

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))

print("+")
print("-")
print("*")
print("/")
calc = input("Operation?")


if(calc == '+'):
    res = int(num1) + int(num2)
elif(calc == '-'):
    res = int(num1) - int(num2)
elif(calc == '*'):
    res = int(num1) * int(num2)
elif(calc == '/'):
    res = int(num1) / int(num2)
else:
    print("Error!")






print (res)





