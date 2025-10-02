#////

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        print(self.owner + " | " + str(self.balance))
        self.balance += 5
        print(f"Wait...\nNew balance: {self.balance}")

    def took(self, amount):
        print(self.owner + " | " + str(self.balance))
        self.balance -= amount
        print(f"Wait...\nNew balance: {self.balance}")

    def info(self):
        print(f"INFO:\n{self.owner} | {str(self.balance)}")


owner1 = BankAccount("Owner1", 0)
#owner1.deposit()
#owner1.took(15)
owner1.info()