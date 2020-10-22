class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def transfer(self, amount, account2):   # Transfer an amout money from account1 to account2
        self.balance -= amount              # Updates the balance of the account you transfer money from
        account2.balance += amount          # Updates the balance of the recipient of the money

    def print_info(self):
        first = self.first_name; last = self.last_name
        number = self.number; balance = self.balance
        s = f'{first} {last}, {number}, balance: {balance}'
        print(s)

def test_BankAccountP():
    account1 = BankAccountP('Paul', 'McCartney', '1337', 420000)
    account2 = BankAccountP('Ringo', 'Starr', '666', 690000)
    assert account1.get_balance() == 420000, 'get_balance failed'
    account1.deposit(5000)
    assert account1.get_balance() == 425000, 'deposit failed'
    account1.withdraw(10000)
    assert account1.get_balance() == 415000, 'withdraw failed'
    account1.transfer(10000, account2)
    assert account1.get_balance() == 405000 and account2.get_balance() == 700000, 'transfer failed'

test_BankAccountP()

"""
Terminal > AccountP.py

"""
