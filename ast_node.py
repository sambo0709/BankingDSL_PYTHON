# Author: Temesgen Gadore
# Date: April 2026
# Class: CSS335
# Assignment: Final Project
# File Name: ast_node.py
# Description: Defines the ASTNode class for the Banking DSL.
#              Represents a single node in the Abstract Syntax
#              Tree built by the Parser.
# References:lecture notes
# We certify that the Python file I am submitting is my own.
# None of it is copied from any source or any person.
# Signed: Temesgen Gadore

# ASTNODE


class ASTNode:

    # node type constants mirror the Banking DSL statements
    PROGRAM  = "PROGRAM"
    DEPOSIT  = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    BALANCE  = "BALANCE"
    CREATE   = "CREATE"
    EXIT     = "EXIT"

    # constructor stores node type, optional value, and
    # an empty list of children
    def __init__(self, node_type, value=None):
        self.__node_type = node_type
        self.__value = value
        self.__children = []

    # getter for node type
    def get_type(self):
        return self.__node_type

    # getter for node value
    def get_value(self):
        return self.__value

    # getter for children list
    def get_children(self):
        return self.__children

    # adds a child ASTNode to this node's children list
    def add_child(self, node):
        self.__children.append(node)

    # returns a readable string representation for debugging
    def __str__(self):
        return f"ASTNode({self.__node_type}, {self.__value})"
