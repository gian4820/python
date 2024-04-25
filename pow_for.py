
def power(base, pow):
    result = 1
    for index  in range(pow):
        result = result * base
    
    return result
base = int( input ("Add the base: "))
pow = int(input ("Add the pow: "))


print (power(base,pow))
