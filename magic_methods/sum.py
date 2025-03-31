class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        

    def __add__(self, balance2):
        return BankAccount(self.balance + balance2.balance)


a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)



