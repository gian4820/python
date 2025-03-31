class Calculator:
    #your code goes here
    @staticmethod
    def add(n1,n2):
        tot=n1+n2
        
        print("Total:")
        return tot
        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))