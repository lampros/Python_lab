from __future__ import annotations

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def print_details(self):
        print(f"The account of {self.name} has balance {self.balance}")

    def money_transfer(self, account: BankAccount, amount):
        if amount > 0 and self.balance >= amount :
            self.balance -= amount
            account.balance += amount
        else:
            print(f"impossible action")


         
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def print_details(self):
        super().print_details()
        print(f"The interest of the savings account is {self.interest}")

    def apply_interest(self):
        self.balance = self.balance + self.interest * self.balance


class BusinessAccount(BankAccount):
    def __init__(self, name, balance, brand_name):
        super().__init__(name, balance)
        self.brand_name = brand_name

    def print_details(self):
        super().print_details()
        print(f"The brand name of the company that owes the account is {self.brand_name}")



lampros_savings = SavingsAccount("Lampros", 1000, 0.05)
maria_business = BusinessAccount("Maria", 2000, "DataTech")

lampros_savings.print_details()
maria_business.print_details()

lampros_savings.money_transfer(maria_business, 300)
lampros_savings.apply_interest()

lampros_savings.print_details()
maria_business.print_details()