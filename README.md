# Banking DSL
### CSS335 Programming Language Paradigms — Final Project
**Authors:** Samuel Boye & Temesgen Gadore  
**Institution:** Concordia University St. Paul  
**Instructor:** Professor Dawn Duerre  
**Date:** April 2026

---

## Overview
Banking is a Domain-Specific Language (DSL) built in Python that simulates basic banking operations. Users interact with the program by typing simple commands. Each command is processed through a full compiler pipeline: Lexer → Parser → AST → Interpreter.

---

## Features
- Deposit funds into an account
- Withdraw funds from an account
- Check account balance
- Create a new account
- 9 pre-created accounts loaded at startup
- Full lexer/parser/AST output displayed for every command
- DSL specification tests using Python `unittest`

---

## Project Structure
```
BankingDSL_PYTHON/
├── banking.py          # Main entry point and menu loop
├── bank_account.py     # BankAccount class
├── banking_token.py    # Token class and token type constants
├── lexer.py            # Lexer — tokenizes input
├── ast_node.py         # ASTNode class
├── parser.py           # Parser — builds AST from tokens
├── interpreter.py      # Interpreter — executes AST
├── spec_testing.py     # DSL specification tests
└── banking.ebnf        # EBNF grammar for the Banking DSL
```

---

## How to Run

### Requirements
- Python 3.9 or later
- No external libraries needed

### Run the main Banking program
```bash
python3 banking.py
```

### Run the specification tests
```bash
python3 spec_testing.py
```

---

## Banking DSL Commands
| Command | Example |
|---|---|
| `deposit [account_id] [amount]` | `deposit SB473189 500` |
| `withdraw [account_id] [amount]` | `withdraw SB473189 200` |
| `balance [account_id]` | `balance SB473189` |
| `create [first_name] [last_name] [amount]` | `create John Doe 1000` |
| `exit` / `quit` / `end` | `exit` |

### Account ID Format
Account IDs are auto-generated: first letter of first name + first letter of last name (uppercased) + 6 random digits.  
Example: Samuel Boye → `SB473189`

---

## Pipeline
```
User Input
    ↓
Lexer (banking_token.py, lexer.py)
    ↓
Token List
    ↓
Parser (parser.py, ast_node.py)
    ↓
Abstract Syntax Tree (AST)
    ↓
Interpreter (interpreter.py)
    ↓
BankAccount Operations (bank_account.py)
    ↓
Output
```

---

## EBNF Grammar (banking.ebnf)
```
program       = { statement } ;
statement     = deposit_stmt | withdraw_stmt | balance_stmt
              | create_stmt | exit_stmt ;
deposit_stmt  = "deposit", account_id, amount ;
withdraw_stmt = "withdraw", account_id, amount ;
balance_stmt  = "balance", account_id ;
create_stmt   = "create", first_name, last_name, amount ;
exit_stmt     = "exit" | "quit" | "end" ;
account_id    = letter, letter, digit, digit, digit,
                digit, digit, digit ;
amount        = float | integer ;
```

---

## Specification Tests
Run `spec_testing.py` and select from the menu:
1. Run all tests
2. Run deposit test
3. Run withdraw test
4. Run balance test
5. Run create account test
6. Run account number format test

All 7 tests should pass with `OK`.

---

## References
- Python unittest documentation: https://docs.python.org/3/library/unittest.html
- Extended Backus-Naur Form: https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form
- Duerre, Dawn. CSS335 Course Materials. Concordia University St. Paul, Spring 2026.
