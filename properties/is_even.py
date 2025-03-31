class Number:
    def __init__(self, num):
        self.num = num
        
    #your code goes here
    @property
    def isEven(self):
        if self.num%2==0:
            return True
        else:
            return False
 
num = Number(int(input()))
print(num.isEven)