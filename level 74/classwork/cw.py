class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """შეაქვს თანხა ანგარიშზე"""
        self.balance += amount
        print(f"{amount} ლარი დაემატა ანგარიშზე.")

    def withdraw(self, amount):
        """აიღებს თანხას ანგარიშიდან"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} ლარი იქნა გამოღებული.")
        else:
            print("არასაკმარისი თანხა.")

    def show_balance(self):
        """გაჩვენებს ანგარიშის მდგომარეობას"""
        print(f"{self.owner}: {self.balance} ლარი")