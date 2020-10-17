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

    def parseExp(self):
        tok = self.scanner.getNextToken()
        return parseExp(tok)

    def parseExp(self,token1):
        if(token1 == None):
            return Nil
        type1 = token1.getType()
        if(type1 == TokenType.LPAREN):
            return parseRest()
        elif(type1 == TokenType.FALSE):
            return BoolLit(False)
        elif(type1 == TokenType.TRUE):
            return BoolLit(True)
        elif(type1 == TokenType.QUOTE):
            return Cons(Ident("\'"),parseExp())
        elif(type1 == TokenType.INT):
            return IntLit(token1.getIntVal())
        elif(type1 == TokenType.STRING):
            return StrLit(token1.getIntVal())
        elif(type1 == TokenType.IDENT):
            return Ident(token1.getName())
        else:
            self.error("Token did not match any of the given types")
            return None

    def parseRest(self):
        tok = self.scanner.getNextToken()
        return parseRest(tok)

    def parseRest(self,token1):
        type1 = token1.getType()
        if(type1 == TokenType.RPAREN):
            return Nil
        token2 = self.scanner.getNextToken()
        type2 = token2.getType()
        if(type1 == TokenType.LPAREN):
            if(type2 == TokenType.RPAREN):
                return Cons(Nil,parseRest()) 
            else:
                return Cons(Cons(parseExp(token2),parseRest()),parseRest())
        if(type2 == TokenType.DOT):
            return Cons(parseExp(token1,parseExp()))
        elif(type2 == TokenType.RPAREN):
            return Cons(parseExp(token1),Nil)
        else:
            return Cons(parseExp(token1),Cons(parseExp(token2),parseRest()))

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
