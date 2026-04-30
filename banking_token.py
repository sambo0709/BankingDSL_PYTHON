# Author: 
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: token.py
# Description: Defines the Token class for the Banking DSL.
#              Stores token type constants and type/value
#              pairs produced by the Lexer.
# References:
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: 

#TOKEN           


class Token:

    # token type constants used across Lexer and Parser
    DEPOSIT    = "DEPOSIT"
    WITHDRAW   = "WITHDRAW"
    BALANCE    = "BALANCE"
    CREATE     = "CREATE"
    EXIT       = "EXIT"
    ACCOUNT_ID = "ACCOUNT_ID"
    AMOUNT     = "AMOUNT"
    NAME       = "NAME"
    EOF        = "EOF"
    UNKNOWN    = "UNKNOWN"

    # constructor stores the token type and its lexeme value
    def __init__(self, token_type, value):
        self.__token_type = token_type
        self.__value = value

    # getter for token type
    def get_type(self):
        return self.__token_type

    # getter for token value/lexeme
    def get_value(self):
        return self.__value

    # returns a readable string representation of the token
    def __str__(self):
        return f"Token({self.__token_type}, {self.__value})"
