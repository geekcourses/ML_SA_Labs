# ------------------------ accounts with dictionaries ------------------------ #
# def deposit(account, amount):
#     account['balance'] += amount

# account1 = {
#     'owner':'Maria',
#     'balance': 1000
# }

# account2 = {
#     'owner':'Pesho',
#     'balance': 2000
# }

# deposit(account1, 100)
# deposit(account2, 200)

# print( account1 )
# print( account2 )



# --------------------------- accounts with objects -------------------------- #
class BankAccount:
    # class attribute
    count = 0

    # instance method
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.count += 1

    def __str__(self):
        return f'Owner: {self.owner}, Balance: {self.balance}'

    def __add__(self, other):
        return self.balance + other.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        print(self)
        if self.balance>=amount:
            self.balance -= amount
        else:
            print('Not enough money')

# # Create an instance of the BankAccount class
account1 = BankAccount('Maria', 1000)
# BankAccount.__init__( account1, 'Maria', 1000)

account2 = BankAccount('Pesho', 2000)
# create_account( account2, 'Pesho', 2000)

print( account1 )
print( account2 )

print( account1 + account2 )


# account1.deposit(100)
# account2.deposit(1000)

# # call instance method
# account1.withdraw(1000)

# # access instance attribute
# print(account1.owner)


# # access class attribute
# print( f'Accounts created: {BankAccount.count}' )