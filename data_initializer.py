"""
By running this script initialize the bank account holder data and write it into the file
"""

import bank_pb2
import sys
from barnum import gen_data


def open_account(person):
    """
    In this function create a person object with dummy data
    :param person: Proto buffer data structure object
    :return: None
    """
    person.name = gen_data.create_name()[0]
    person.account_no = gen_data.create_cc_number(length=10)[1][0]
    person.pin_no = gen_data.create_pw(length=2)
    person.amount = 5000
    print "Thank You", person.name, "to open your account..."

# Entry Point of the script
if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "Enter the file name"
    sys.exit(-1)

bank_account = bank_pb2.BankAccounts()

# Read the data from file.
try:
    account_holder_file = open(sys.argv[1], "rb")
    bank_account.ParseFromString(account_holder_file.read())
    account_holder_file.close()
except IOError:
    print sys.argv[1] + ": File not Exist. Creating a new one."

# Initially we create two accounts.
open_account(bank_account.person.add())
open_account(bank_account.person.add())

# Write the data into the file.
account_holder_file = open(sys.argv[1], "wb")
account_holder_file.write(bank_account.SerializeToString())
account_holder_file.close()
