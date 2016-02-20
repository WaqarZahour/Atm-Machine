"""In this script take the pin number of particular account holder from file
   and do the operations like amount transfer, compare account
"""

import os
import bank_pb2


class BankAtm(object):
    """ Welcome to Bank Atm machine where user can multiple operations """

    def __init__(self):
        """ Default Constructor """
        self.person_list = []
        self.account_holder = None
        self.file_name = "account_holders"
        self.bank_account = bank_pb2.BankAccounts()

    def is_account_holder_exist(self, pin_no, is_account_number=False):
        """
        If Account Holder Exist Return that Account Holder
        :param pin_no: Can be account number or atm pin number
        :param is_account_number: Can be True or False
        :return: person object or None
        """
        for person in self.person_list:
            if not is_account_number and pin_no == person.pin_no:
                return person
            if is_account_number and pin_no == person.account_no:
                return person
        return None

    def load_account(self):
        """ Verify the User exist in the list switch to that account """

        # Read the data from file.
        with open(self.file_name, "rb") as f:
                self.bank_account.ParseFromString(f.read())
        self.person_list = self.bank_account.person

    def print_bank_info(self):
        """ In this function display the account holder information """
        print "Person"
        print "  Name:", self.account_holder.name
        print "  Pin:", self.account_holder.pin_no
        print "  Account No:", self.account_holder.account_no
        print "  Amount", self.account_holder.amount

    def commit_transaction(self):
        """ Update the file if transaction successfully done """

        try:
            file_handler = open(self.file_name, 'w')
        except IOError:
            print 'File cannot be opened:', self.file_name
            exit()

        file_handler.write(self.bank_account.SerializeToString())
        file_handler.close()

    def cash_withdraw(self):
        """ Amount withdraw from my account  """
        amount = raw_input('Enter the Amount >>> ')
        try:
            amount = int(amount)
            if amount > self.account_holder.amount:
                raise ValueError    # raise exception if user enter the wrong value
            else:
                self.account_holder.amount -= amount
                self.commit_transaction()
                print "Your transaction has been done successfully"
        except ValueError:
            print "********** Error Message **********\nYou enter wrong amount"

        self.another_transecton()

    def transfer_money(self):
        """ If to_account holder exist transfer amount """

        account_no = raw_input('Enter the Account Number >>> ')
        to_account_holder = self.is_account_holder_exist(account_no, is_account_number=True)

        if to_account_holder is None:
            print "Account Holder Doesn't Exist"
        if to_account_holder.account_no == self.account_holder.account_no:
            print "You cannot transfer amount into your account"
        else:
            amount = raw_input('Enter the Amount >>> ')
            try:
                amount = int(amount)
                if amount > self.account_holder.amount:
                    raise ValueError    # raise exception if user enter the wrong value
                else:
                    self.account_holder.amount -= amount
                    to_account_holder.amount += amount
                    self.commit_transaction()
                    print "Your transaction has been done successfully"
            except ValueError:
                print "********** Error Message **********\nYou enter wrong amount"

        self.another_transecton()

    def account_detail(self):
        """ Show the account detail like name , balance """
        self.print_bank_info()
        self.another_transecton()

    @classmethod
    def exit_menu(cls):
        """ Exit from the menu """
        print "Thank your for using our services"
        exit()

    def another_transecton(self):
        """ Prompt for asking another transaction """
        user_input = raw_input('Do you want another transection [press y] >>> ')
        if user_input == 'y':
            self.show_menu()

    def show_menu(self):
        """ Bank Atm Menu """
        os.system('clear')
        print "********** Welcome to Atm **********"
        print "Press 1 for Cash Withdraw"
        print "Press 2 for Transfer Money"
        print "Press 3 for Account Detail"
        print "Press 4 for Exit"

        user_selected_option = raw_input('Enter the Option >>> ')
        try:
            user_selected_option = int(user_selected_option)
            if user_selected_option > 4 or user_selected_option < 1:
                raise ValueError    # raise exception if user enter the wrong value
            {
                1: self.cash_withdraw,
                2: self.transfer_money,
                3: self.account_detail,
                4: BankAtm.exit_menu
            }[user_selected_option]()
        except ValueError:
            print "********** Error Message **********\nThe option doesn't exist"
            self.another_transecton()

    def pin_prompt(self):
        """ Menu to enter the pin number """
        os.system('clear')
        print "********** Enter Your Pin **********"
        pin_no = raw_input('>>> ')
        try:
            self.account_holder = self.is_account_holder_exist(pin_no)
            if self.account_holder is not None:
                self.show_menu()
            else:
                raise ValueError
        except ValueError:
            print "********** Error Message **********\nYou Enter wrong pin number"


def main():
    """ This is the main entry point to enter the bank atm"""
    bank_atm = BankAtm()
    bank_atm.load_account()
    bank_atm.pin_prompt()

if __name__ == "__main__":
    main()
