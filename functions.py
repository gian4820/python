from unittest import result


def say_hi():
    print ("Hello world")

say_hi()


#function with parameter
def hi(name):
    print("Hi, my name is " + name)
hi("Jhon")


#return
def cube(num):
    return num * num * num

result = cube(4)
print(result)

