# Author: Samuel Boye
# Date: 23April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: lexer.py
# Description: Defines the Lexer class for the Banking DSL.
#              Tokenizes a line of input into a list of
#              Token objects for the Parser to consume.
# References:Calc program from class and lecture notes.
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: Samuel Boye

import re
from banking_token import Token

#LEXER



class Lexer:

    # maps keyword strings to their token types
    KEYWORDS = {
        "deposit":  Token.DEPOSIT,
        "withdraw": Token.WITHDRAW,
        "balance":  Token.BALANCE,
        "create":   Token.CREATE,
        "exit":     Token.EXIT,
        "quit":     Token.EXIT,
        "end":      Token.EXIT
    }

    # constructor takes the raw input string to tokenize
    def __init__(self, text):
        self.__text = text.strip()
        self.__tokens = []

    # getter for the token list
    def get_tokens(self):
        return self.__tokens

    # tokenizes the input string into a list of Token objects
    # and appends an EOF token at the end
    def tokenize(self):
        words = self.__text.split()
        for word in words:
            token = self.__classify(word)
            self.__tokens.append(token)
        self.__tokens.append(Token(Token.EOF, None))
        return self.__tokens

    # classifies a single word into its correct Token type
    # checks keywords, account ID, float, integer, name
    def __classify(self, word):
        if word.lower() in self.KEYWORDS:
            result = Token(self.KEYWORDS[word.lower()], word)
        elif re.fullmatch(r'[A-Za-z]{2}[0-9]{6}', word):
            result = Token(Token.ACCOUNT_ID, word)
        elif re.fullmatch(r'[0-9]+\.[0-9]+', word):
            result = Token(Token.AMOUNT, float(word))
        elif re.fullmatch(r'[0-9]+', word):
            result = Token(Token.AMOUNT, int(word))
        elif re.fullmatch(r'[A-Za-z]+', word):
            result = Token(Token.NAME, word)
        else:
            result = Token(Token.UNKNOWN, word)
        return result
