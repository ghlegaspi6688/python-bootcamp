class BankAcount:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= self.amount

    def deposit(self, amount):
        self.__balance += self.amount

    def print_balance(self):
        print(self.balance)


balance = int(input("Enter Amount: "))

