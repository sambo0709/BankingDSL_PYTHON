# Author: 
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: interpreter.py
# Description: Defines the Interpreter class for the Banking
#              DSL. Walks the AST produced by the Parser and
#              executes each node against the accounts list.
# References:
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: 

from ast_node import ASTNode
from bank_account import BankAccount

#INTERPRETER       


class Interpreter:

    # constructor takes the list of pre-created BankAccount
    # objects to operate on
    def __init__(self, accounts):
        self.__accounts = accounts

    # getter for accounts list
    def get_accounts(self):
        return self.__accounts

    # main entry point — walks the PROGRAM node's children
    # and interprets each statement, printing the result
    def interpret(self, ast):
        result = ""
        for node in ast.get_children():
            result = self.__execute(node)
            print(result)
        return result

    # routes each AST node to the correct execution method
    def __execute(self, node):
        node_type = node.get_type()
        if node_type == ASTNode.DEPOSIT:
            result = self.__execute_deposit(node)
        elif node_type == ASTNode.WITHDRAW:
            result = self.__execute_withdraw(node)
        elif node_type == ASTNode.BALANCE:
            result = self.__execute_balance(node)
        elif node_type == ASTNode.CREATE:
            result = self.__execute_create(node)
        elif node_type == ASTNode.EXIT:
            result = self.__execute_exit()
        else:
            result = "Unknown statement."
        return result

    # searches accounts list for a matching account number
    # returns the account if found, None otherwise
    def __find_account(self, account_id):
        found = None
        for account in self.__accounts:
            if account.get_account_number() == account_id:
                found = account
        return found

    # executes a DEPOSIT node — finds account and deposits
    def __execute_deposit(self, node):
        children = node.get_children()
        account_id = children[0].get_value()
        amount = children[1].get_value()
        account = self.__find_account(account_id)
        if account is not None:
            result = account.deposit(amount)
        else:
            result = f"Account {account_id} not found."
        return result

    # executes a WITHDRAW node — finds account and withdraws
    def __execute_withdraw(self, node):
        children = node.get_children()
        account_id = children[0].get_value()
        amount = children[1].get_value()
        account = self.__find_account(account_id)
        if account is not None:
            result = account.withdraw(amount)
        else:
            result = f"Account {account_id} not found."
        return result

    # executes a BALANCE node — finds account and returns
    # the current balance
    def __execute_balance(self, node):
        children = node.get_children()
        account_id = children[0].get_value()
        account = self.__find_account(account_id)
        if account is not None:
            result = account.check_balance()
        else:
            result = f"Account {account_id} not found."
        return result

    # executes a CREATE node — creates a new BankAccount
    # and appends it to the accounts list
    def __execute_create(self, node):
        children = node.get_children()
        first_name = children[0].get_value()
        last_name = children[1].get_value()
        amount = children[2].get_value()
        new_account = BankAccount(first_name, last_name, amount)
        self.__accounts.append(new_account)
        result = (f"Account created for "
                  f"{first_name} {last_name}. "
                  f"Account #: "
                  f"{new_account.get_account_number()} "
                  f"| Balance: ${amount:.2f}")
        return result

    # executes an EXIT node — returns the EXIT signal string
    def __execute_exit(self):
        return "EXIT"
