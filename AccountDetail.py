import csv
import time
class AccountDetail:

    accnt_details = []

    def __init__(self):

        with open('AccountTransactions.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                self.accnt_details.append({
                    'acct_num': row[0],
                    'date': time.strptime(row[1], '%b-%y'),
                    'bal': row[2]
                })

    def get_account_num(self):
        return self.AccountNum

    def get_balance(self, date):
        for det in self.accnt_details:
            if det["month"] == date:
                return det
        return None