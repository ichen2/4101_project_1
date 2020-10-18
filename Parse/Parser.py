# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from Tokens import TokenType
# gerald said to import these
from Tree import *

class Parser:
    def __init__(self, s):
        self.scanner = s
        self.nodeFalse = BoolLit(False)
        self.nodeTrue = BoolLit(True)
        self.nodeNil = Nil()

    def parseExp(self):
        tok = self.scanner.getNextToken()
        return self.parseExpOverloaded(tok)

    def parseExpOverloaded(self,token1):
        if(token1 == None):
            return self.nodeNil
        type1 = token1.getType()
        if(type1 == TokenType.LPAREN):
            return self.parseRest()
        elif(type1 == TokenType.FALSE):
            return self.nodeFalse
        elif(type1 == TokenType.TRUE):
            return self.nodeTrue
        elif(type1 == TokenType.QUOTE):
            return Cons(Ident("\'"),self.parseExp())
        elif(type1 == TokenType.INT):
            return IntLit(token1.getIntVal())
        elif(type1 == TokenType.STR):
            return StrLit(token1.getStrVal())
        elif(type1 == TokenType.IDENT):
            return Ident(token1.getName())
        else:
            self.error("Token did not match any of the given types")
            return None

    def parseRest(self):
        tok = self.scanner.getNextToken()
        return self.parseRestOverloaded(tok)

    def parseRestOverloaded(self,token1):
        type1 = token1.getType()
        if(type1 == TokenType.RPAREN):
            return self.nodeNil
        token2 = self.scanner.getNextToken()
        type2 = token2.getType()
        if(type1 == TokenType.LPAREN):
            if(type2 == TokenType.RPAREN):
                return Cons(self.nodeNil,self.parseRest()) 
            else:
                return Cons(Cons(self.parseExpOverloaded(token2),self.parseRest()),self.parseRest())
        elif(type1 == TokenType.DOT):
            c = self.parseExpOverloaded(token2)
            self.parseRest()
            return c
        if(type2 == TokenType.DOT):
            # return Cons(self.parseExpOverloaded(token1),self.parseExp())
            c = Cons(self.parseExpOverloaded(token1),self.parseExp())
            self.parseRest()
            return c
        elif(type2 == TokenType.RPAREN):
            return Cons(self.parseExpOverloaded(token1),self.nodeNil)
        else:
            return Cons(self.parseExpOverloaded(token1),Cons(self.parseExpOverloaded(token2),self.parseRest()))

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
