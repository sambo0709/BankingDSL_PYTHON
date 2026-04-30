# Author: Temesgen Gadore
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: parser.py
# Description: Defines the Parser class for the Banking DSL.
#              Takes the token list from the Lexer and builds
#              an Abstract Syntax Tree (AST) from it.
# References:Calc program from class and lecture notes.
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: Temesgen Gadore

from banking_token import Token
from ast_node import ASTNode

# PARSER

class Parser:

    # constructor takes the token list produced by the Lexer
    def __init__(self, tokens):
        self.__tokens = tokens
        self.__pos = 0

    # returns the current token without consuming it
    def __current(self):
        return self.__tokens[self.__pos]

    # consumes and returns the current token, advances pos
    # returns EOF token safely if already at end of list
    def __consume(self):
        if self.__pos < len(self.__tokens):
            token = self.__tokens[self.__pos]
            self.__pos += 1
        else:
            token = Token(Token.EOF, None)
        return token

    # parses the full token list and returns a PROGRAM node
    # as the root of the AST
    def parse(self):
        root = ASTNode(ASTNode.PROGRAM)
        while self.__current().get_type() != Token.EOF:
            statement = self.__parse_statement()
            if statement is not None:
                root.add_child(statement)
        return root

    # routes to the correct parse method based on token type
    def __parse_statement(self):
        token_type = self.__current().get_type()
        if token_type == Token.DEPOSIT:
            result = self.__parse_deposit()
        elif token_type == Token.WITHDRAW:
            result = self.__parse_withdraw()
        elif token_type == Token.BALANCE:
            result = self.__parse_balance()
        elif token_type == Token.CREATE:
            result = self.__parse_create()
        elif token_type == Token.EXIT:
            result = self.__parse_exit()
        else:
            self.__consume()
            result = None
        return result

    # parses: deposit <account_id> <amount>
    # builds a DEPOSIT node with account_id and amount kids
    def __parse_deposit(self):
        self.__consume()
        account_token = self.__consume()
        amount_token = self.__consume()
        if (account_token.get_type() == Token.EOF or
                amount_token.get_type() == Token.EOF):
            print("Usage: deposit [account_id] [amount]")
            result = None
        else:
            node = ASTNode(ASTNode.DEPOSIT)
            node.add_child(ASTNode(ASTNode.DEPOSIT,
                                   account_token.get_value()))
            node.add_child(ASTNode(ASTNode.DEPOSIT,
                                   amount_token.get_value()))
            result = node
        return result

    # parses: withdraw <account_id> <amount>
    # builds a WITHDRAW node with account_id and amount kids
    def __parse_withdraw(self):
        self.__consume()
        account_token = self.__consume()
        amount_token = self.__consume()
        if (account_token.get_type() == Token.EOF or
                amount_token.get_type() == Token.EOF):
            print("Usage: withdraw [account_id] [amount]")
            result = None
        else:
            node = ASTNode(ASTNode.WITHDRAW)
            node.add_child(ASTNode(ASTNode.WITHDRAW,
                                   account_token.get_value()))
            node.add_child(ASTNode(ASTNode.WITHDRAW,
                                   amount_token.get_value()))
            result = node
        return result

    # parses: balance <account_id>
    # builds a BALANCE node with account_id as child
    def __parse_balance(self):
        self.__consume()
        account_token = self.__consume()
        if account_token.get_type() == Token.EOF:
            print("Usage: balance [account_id]")
            result = None
        else:
            node = ASTNode(ASTNode.BALANCE)
            node.add_child(ASTNode(ASTNode.BALANCE,
                                   account_token.get_value()))
            result = node
        return result

    # parses: create <first_name> <last_name> <amount>
    # builds a CREATE node with name and amount as children
    def __parse_create(self):
        self.__consume()
        first_token = self.__consume()
        last_token = self.__consume()
        amount_token = self.__consume()
        if (first_token.get_type() == Token.EOF or
                last_token.get_type() == Token.EOF or
                amount_token.get_type() == Token.EOF):
            print("Usage: create [first_name] [last_name] [amount]")
            result = None
        else:
            node = ASTNode(ASTNode.CREATE)
            node.add_child(ASTNode(ASTNode.CREATE,
                                   first_token.get_value()))
            node.add_child(ASTNode(ASTNode.CREATE,
                                   last_token.get_value()))
            node.add_child(ASTNode(ASTNode.CREATE,
                                   amount_token.get_value()))
            result = node
        return result

    # parses: exit | quit | end
    # builds and returns an EXIT node
    def __parse_exit(self):
        self.__consume()
        return ASTNode(ASTNode.EXIT)