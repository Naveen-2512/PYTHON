
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            balance = self.get_balance()
            if amount <= balance:
                super().withdraw(amount)
            else:
                super().withdraw(balance)
                print("Overdraft used:", amount - balance)
                print("Overdraft limit:", self.overdraft_limit)
        else:
            print("Overdraft limit exceeded.")


def main():
    savings = SavingsAccount("Naveen", 5000, 4)
    current = CurrentAccount("Priya", 3000, 2000)

    print("SAVINGS ACCOUNT")
    savings.display()
    savings.deposit(1000)
    savings.withdraw(500)
    print("Final Balance:", savings.get_balance())

    print("\nCURRENT ACCOUNT")
    current.display()
    current.withdraw(4000)
    print("Remaining Balance:", current.get_balance())


if __name__ == "__main__":
    main()
