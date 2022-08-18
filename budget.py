class Category:
    # wow! this attribute really messed me up
    # it seems all instances of Category were sharing the same
    # ledger?!?
    #ledger = []

    def __init__(self, name):
        if name is None:
            raise TypeError("name cannot be None")
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self._validate_amount(amount)
        tx = {"amount": amount, "description": description}
        self.ledger.append(tx)

    def withdraw(self, amount, description=""):
        self._validate_amount(amount)
        if not self.check_funds(amount):
            return False
        tx = {"amount": -amount, "description": description}
        self.ledger.append(tx)
        return True

    def get_balance(self):
        total = 0
        for tx in self.ledger:
            total += tx['amount']
        return total

    def transfer(self, amount, category):
        self._validate_amount(amount)
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False

    def _validate_amount(self, amount):
        if type(amount) not in [int, float]:
            raise TypeError("amount must be type int")
        if amount < 0:
            raise ValueError("amount cannot be a negative number")

    def __repr__(self):
        return "Not Implemented"

def create_spend_chart(categories):
    pass
