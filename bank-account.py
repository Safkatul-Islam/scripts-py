class BankAccount:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Opening balance can't be negative")
        self.name = name
        self.balance = balance
        self.history = [f"Opened with ${balance:.2f}"]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.history.append(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount:
            self.history.append(f"Failed withdrawal of ${amount:.2f} (insufficient funds)")
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.history.append(f"Withdrew ${amount:.2f}")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history.copy()

    def __str__(self):
        return f"BankAccount({self.name}, ${self.balance:.2f})"


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)

print(acc.get_balance())    # 1300
print(acc.get_history())
print(acc)                  # BankAccount(Alice, $1300.00)