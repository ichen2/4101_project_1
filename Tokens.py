from enum import Enum

class TokenType(Enum) :
    QUOTE = 1
    LPAREN = 2
    RPAREN = 3
    DOT = 4
    TRUE = 5
    FALSE = 6
    INT = 7
    STRING = 8
    IDENT = 9
    
class Token :
    def __init__(self, TokenType) :
        self.tt = TokenType

class IntToken(Token) :
    def __init__(self, value) :
        self.tt = TokenType.INT
        self.intVal = value

class StringToken(Token) :
    def __init__(self, value) :
        self.tt = TokenType.STRING
        self.stringVal = value

class IdentToken(Token) :
    def __init__(self, value) :
        self.tt = TokenType.IDENT
        self.identVal = value