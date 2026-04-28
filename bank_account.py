# Author: 
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: bank_account.py
# Description: Defines the BankAccount class for the Banking
#              DSL. Handles account data and operations:
#              deposit, withdraw, and balance check.
# References:
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: 

import random

#BANKACCOUNT


class BankAccount:

    # constructor initializes a bank account with private
    # fields and auto-generates the account number
    def __init__(self, first_name, last_name, balance=0.0):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = self.__generate_account_number()
        self.__balance = balance

    # generates account number: first letter of first and
    # last name (uppercased) followed by 6 random digits
    def __generate_account_number(self):
        letters = (self.__first_name[0] +
                   self.__last_name[0]).upper()
        digits = str(random.randint(100000, 999999))
        result = letters + digits
        return result

    # ------ GETTERS ------

    # getter for first name
    def get_first_name(self):
        return self.__first_name

    # getter for last name
    def get_last_name(self):
        return self.__last_name

    # getter for account number
    def get_account_number(self):
        return self.__account_number

    # getter for balance
    def get_balance(self):
        return self.__balance

    # SETTERS

    # setter for first name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # setter for last name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # setter for balance
    def set_balance(self, balance):
        self.__balance = balance

    # METHODS
    # deposits the given amount and returns a result message
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            result = (f"Deposited ${amount:.2f}. "
                      f"New balance: ${self.__balance:.2f}")
        else:
            result = "Deposit amount must be greater than 0."
        return result

    # withdraws the given amount and returns a result message
    def withdraw(self, amount):
        if amount <= 0:
            result = "Withdrawal amount must be greater than 0."
        elif amount > self.__balance:
            result = "Insufficient funds."
        else:
            self.__balance -= amount
            result = (f"Withdrew ${amount:.2f}. "
                      f"New balance: ${self.__balance:.2f}")
        return result

    # returns the current balance as a formatted string
    def check_balance(self):
        return (f"Balance for account "
                f"{self.__account_number}: "
                f"${self.__balance:.2f}")

    # returns a full summary of account info
    def get_account_info(self):
        return (f"Name: {self.__first_name} {self.__last_name}"
                f" | Account #: {self.__account_number}"
                f" | Balance: ${self.__balance:.2f}")
