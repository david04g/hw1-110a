from enum import Enum
import re
class Token(Enum):
    ID     = "ID"
    NUM    = "NUM"
    IGNORE = "IGNORE"
    HNUM   = "HNUM"
    INCR   = "INCR"
    PLUS   = "PLUS"
    MULT   = "MULT"
    SEMI   = "SEMI"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    ASSIGN = "ASSIGN"
    IF     = "IF"
    ELSE   = "ELSE"
    WHILE  = "WHILE"
    INT    = "INT"
    FLOAT  = "FLOAT"


class Lexeme:
    def __init__(self, token:Token, value:str) -> None:
        self.token = token
        self.value = value

    def __str__(self):
        return "(" + str(self.token) + "," + "\"" + self.value + "\"" + ")"    

def idy(l:Lexeme) -> Lexeme:
    return l

keys = {
    "if": Token.IF,
    "else": Token.ELSE,
    "while": Token.WHILE,
    "int": Token.INT,
    "float": Token.FLOAT,
}

def id_or_key(l: Lexeme) -> Lexeme:
    if l.value in keys:
        l.token = keys[l.value]
    return l

tokens = [
        (Token.HNUM,   r"0[xX][0-9a-fA-F]+", idy),
    (Token.INCR,   r"\+\+", idy),
    (Token.PLUS,   r"\+", idy),
    (Token.MULT,   r"\*", idy),
    (Token.SEMI,   r";", idy),
    (Token.LPAREN, r"\(", idy),
    (Token.RPAREN, r"\)", idy),
    (Token.LBRACE, r"\{", idy),
    (Token.RBRACE, r"\}", idy),
    (Token.ASSIGN, r"=", idy),
    (Token.ID,     r"[a-zA-Z_][a-zA-Z_0-9]*", id_or_key),
    (Token.NUM, r"(0|[1-9][0-9]*)(\.[0-9]+)?|\.[0-9]+", idy),
    (Token.IGNORE, r"[ \n\t]+", idy)
]
