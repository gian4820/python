text = input()

def uppercase_decorator(func):
    def wrapper(text):
        #your code goes here
        u= text.upper()
        return func(u)  
    return wrapper
    
@uppercase_decorator    
def display_text(text):
    return(text)
    
print(display_text(text))


