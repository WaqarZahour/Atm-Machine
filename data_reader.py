"""
By running this script display the bank account holder data that is already written in the file
"""

import bank_pb2
import sys


def display_accounts(bank_account):
    """
    In this function diplay the account holder information
    :param bank_account:
    :return:
    """
    for person in bank_account.person:
        print "Person"
        print "  Name:", person.name
        print "  Pin:", person.pin_no
        print "  Account No:", person.account_no
        print "  Amount", person.amount

# Entry Point of the script
if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "Enter the file name"
    sys.exit(-1)

print "***** Account Holders *****"
bank_account = bank_pb2.BankAccounts()

# Read the data from file.
with open(sys.argv[1], "rb") as f:
    bank_account.ParseFromString(f.read())

# Display Accounts.
display_accounts(bank_account)


