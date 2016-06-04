class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number): #pragma: no cover
        return self.accounts.get(account_number)
