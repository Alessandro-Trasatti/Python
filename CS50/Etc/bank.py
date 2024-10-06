# balance = 0 # Global variable 

# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)
    
# def deposit(money):
#     global balance
#     balance += money
    
# def withdraw(money):
#     global balance
#     balance -= money
    
# if __name__ == "__main__":
#     main()

# The same can be done better with OOP
class Account:
    def __init__(self):
        self._balance = 0
        
    @property    
    def balance(self):
        return self._balance
    
    def deposit(self, money):
        self._balance += money
        
    def withdraw(self, money):
        self._balance -= money
        
        
def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.deposit(50)
    print("Balance: ", account.balance)
    
if __name__ == "__main__":
    main()