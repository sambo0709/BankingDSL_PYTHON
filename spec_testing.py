# Author: Samuel Boye, Temesgen Gadore
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: spec_testing.py
# Description: DSL specification tests for the Banking DSL.
#              Tests deposit, withdraw, balance, and account
#              creation using Python's unittest module.
# References: pyhton unittest documentation. 
# https://docs.python.org/3/library/unittest.html
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: Temesgen Gadore, Samuel Boye

import unittest
from bank_account import BankAccount
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

#SPEC TESTING


# test suite for the Banking DSL
class TestBankingDSL(unittest.TestCase):

    # sets up a fresh interpreter and accounts before each test
    def setUp(self):
        self.account = BankAccount("Samuel", "Boye", 1000.00)
        self.accounts = [self.account]
        self.interpreter = Interpreter(self.accounts)
        self.account_id = self.account.get_account_number()

    # helper: runs a command string through the full pipeline
    def run_command(self, command):
        lexer = Lexer(command)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        result = self.interpreter.interpret(ast)
        return result

    # test that a valid deposit increases the balance
    def test_deposit_increases_balance(self):
        self.run_command(f"deposit {self.account_id} 500")
        expected = 1500.00
        actual = self.account.get_balance()
        self.assertEqual(
            actual, expected,
            f"FAIL - deposit test: expected ${expected:.2f}"
            f" but got ${actual:.2f}"
        )

    # test that a valid withdrawal decreases the balance
    def test_withdraw_decreases_balance(self):
        self.run_command(f"withdraw {self.account_id} 200")
        expected = 800.00
        actual = self.account.get_balance()
        self.assertEqual(
            actual, expected,
            f"FAIL - withdraw test: expected ${expected:.2f}"
            f" but got ${actual:.2f}"
        )

    # test that withdrawal with insufficient funds is rejected
    def test_withdraw_insufficient_funds(self):
        result = self.run_command(
            f"withdraw {self.account_id} 9999"
        )
        expected = "Insufficient funds."
        self.assertEqual(
            result, expected,
            f"FAIL - insufficient funds test: "
            f"expected '{expected}' but got '{result}'"
        )

    # test that balance command returns correct balance string
    def test_balance_check(self):
        result = self.run_command(
            f"balance {self.account_id}"
        )
        self.assertIn(
            "1000.00", result,
            f"FAIL - balance test: expected balance of"
            f" $1000.00 in result but got '{result}'"
        )

    # test that create command adds a new account to the list
    def test_create_account(self):
        initial_count = len(self.accounts)
        self.run_command("create Test User 500")
        new_count = len(self.accounts)
        self.assertEqual(
            new_count, initial_count + 1,
            f"FAIL - create test: expected "
            f"{initial_count + 1} accounts but got "
            f"{new_count}"
        )

    # test that account number format is correct (2 letters
    # followed by 6 digits)
    def test_account_number_format(self):
        number = self.account.get_account_number()
        letters_ok = number[:2].isalpha()
        digits_ok = number[2:].isdigit()
        length_ok = len(number) == 8
        self.assertTrue(
            letters_ok and digits_ok and length_ok,
            f"FAIL - account number format test: "
            f"'{number}' is not in correct format"
        )

    # test that deposit with amount of 0 is rejected
    def test_deposit_zero_rejected(self):
        result = self.account.deposit(0)
        expected = "Deposit amount must be greater than 0."
        self.assertEqual(
            result, expected,
            f"FAIL - zero deposit test: "
            f"expected '{expected}' but got '{result}'"
        )


#TEST MENU

# prints the test menu options
def print_test_menu():
    print("\n--- Banking DSL Spec Testing ---")
    print("  1. Run all tests")
    print("  2. Run deposit test")
    print("  3. Run withdraw test")
    print("  4. Run balance test")
    print("  5. Run create account test")
    print("  6. Run account number format test")
    print("  exit / quit / end")
    print("> ", end="")

# runs a specific test by name and prints pass/fail result
def run_single_test(test_name):
    suite = unittest.TestSuite()
    suite.addTest(TestBankingDSL(test_name))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# main function for spec testing — menu loop for test options
def main():
    print_test_menu()
    user_input = input().strip()

    while user_input.lower() not in ("exit", "quit", "end"):
        if user_input == "1":
            unittest.main(
                module=__name__,
                argv=[""],
                exit=False,
                verbosity=2
            )
        elif user_input == "2":
            run_single_test("test_deposit_increases_balance")
        elif user_input == "3":
            run_single_test("test_withdraw_decreases_balance")
        elif user_input == "4":
            run_single_test("test_balance_check")
        elif user_input == "5":
            run_single_test("test_create_account")
        elif user_input == "6":
            run_single_test("test_account_number_format")
        else:
            print("Invalid option. Please try again.")
        print_test_menu()
        user_input = input().strip()

    print("Exiting spec testing. Goodbye!")


if __name__ == "__main__":
    main()
