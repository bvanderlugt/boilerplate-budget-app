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
        ret = f"{self.name:*^30}\n"
        for tx in self.ledger:
            description = tx['description'][:23]
            amount = tx['amount']
            pad_len = max(33 - (len(str(description)) + len(str(amount))), 7)
            ret += f"{description}{amount:>{pad_len}.2f}\n"
        ret += f"Total: {self.get_balance()}"
        return ret

def create_spend_chart(categories):
    ret = "Percentage spent by category\n"
    spent = {}
    total_spent = 0

    # sum the total spent and create a dict to store spent per category 
    for category in categories:
        for tx in category.ledger:
            # check if transaction is a withdraw
            if tx['amount'] < 0:
                total_spent += tx['amount']
                spent[category.name] = spent.get(category.name, 0) + tx['amount']

    # create a list to store category and percentages
    percentages = []
    for key, val in spent.items():
        # This might look wacky but we are:
        # get whole number percent value: (100*(val/total_spent)) 
        # round down to nearest 10's place: x//10*10
        percentage = (100*(val/total_spent))//10 *10
        category = key
        percentages.append((category, percentage))
    for interval in range(100, -1, -10):
        bubbles = ['o' if elem[1] >= interval else ' ' for elem in percentages]
        ret += f"{interval:>3}| {'  '.join(bubbles)}  \n"
    # TODO make this dynamic, probably len(category) * n + whatever we need for
    # margins
    ret += f"{10*'-':>14}\n"
    max_category_name_len = 0

    # we are going to loop through the Category names and print each character
    # vertically
    # so first get the max len of Category names
    for percent in percentages:
        len_name = len(percent[0])
        if len_name > max_category_name_len:
            max_category_name_len = len_name
    # Loop through each Category name and append character to new line
    for i in range(max_category_name_len):
        char_line = []
        for percent in percentages:
            try:
                char_line.append(percent[0][i])
            except IndexError:
                char_line.append(' ')
        ret += f"{' ':>5}{'  '.join(char_line)}\n"
    print(ret)
    return ret
