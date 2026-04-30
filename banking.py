# Author: Samuel Boye, Temesgen Gadore
# Date: 22 April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: banking.py
# Description: Main entry point for the Banking DSL program.
#              Initializes accounts, runs the menu loop, and
#              passes user input through the full pipeline:
#              Lexer -> Parser -> AST -> Interpreter.
# References: used the Calc program from class and lecture notes as a reference for the structure of the main function 
# and the overall flow of the program.
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: Samuel Boye, Temesgen Gadore

from bank_account import BankAccount
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

#MAIN 


# creates and returns a list of 8 pre-created BankAccounts
def initialize_accounts():
    accounts = [
        BankAccount("Samuel",  "Boye",     1500.00),
        BankAccount("Temesgen", "Gadore", 1800.00),
        BankAccount("John",    "Doe",      2000.00),
        BankAccount("Jane",    "Smith",     800.00),
        BankAccount("Alice",   "Johnson",  3200.00),
        BankAccount("Bob",     "Williams",  500.00),
        BankAccount("Clara",   "Brown",    1200.00),
        BankAccount("David",   "Jones",    4500.00),
        BankAccount("Eva",     "Garcia",    950.00),
    ]
    return accounts

# prints all pre-created accounts and their account numbers
def print_accounts(accounts):
    print("\n--- Pre-Created Accounts ---")
    for account in accounts:
        print(account.get_account_info())
    print("----------------------------\n")

# prints the available Banking DSL command options
def print_menu():
    print("\nEnter a Banking DSL command:")
    print("  deposit  [account_id] [amount]")
    print("  withdraw [account_id] [amount]")
    print("  balance  [account_id]")
    print("  create   [first_name] [last_name] [amount]")
    print("  exit / quit / end")
    print("> ", end="")

# processes a single line of input through the full pipeline
# Lexer -> tokens -> Parser -> AST -> Interpreter -> output
def process_input(user_input, interpreter):
    lexer = Lexer(user_input)
    tokens = lexer.tokenize()
    print("\n-- Tokens --")
    for token in tokens:
        print(f"  {token}")
    parser = Parser(tokens)
    ast = parser.parse()
    print("\n-- AST --")
    for node in ast.get_children():
        print(f"  {node}")
        for child in node.get_children():
            print(f"    {child}")
    print("\n-- Result --")
    result = interpreter.interpret(ast)
    return result

# main function — initializes accounts and runs the menu
# loop until user enters an exit keyword
def main():
    accounts = initialize_accounts()
    print_accounts(accounts)
    interpreter = Interpreter(accounts)

    print_menu()
    user_input = input().strip()

    while user_input.lower() not in ("exit", "quit", "end"):
        process_input(user_input, interpreter)
        print_menu()
        user_input = input().strip()

    print("\nThank you for using Banking by Sam and Teme. Goodbye!")


if __name__ == "__main__":
    main()
