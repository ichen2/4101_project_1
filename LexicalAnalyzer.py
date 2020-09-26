from Tokens import *

class LexicalAnalyzer :

    def __init__( self, fileName ) :
        self.inFile = open(fileName, 'r')
        self.tokens = []

    def analyze(self) :
        for line in self.infile:
            currString = ""
            currType = ""
            for letter in line :
                if currType != "" :
                    if letter == "\"" :
                        currType = "string"
                        self.tokens.append(Token(TokenType.QUOTE))
                elif currType == "string" :
                    if letter == "\"" :
                        currType = ""
                        self.tokens.append(Token(TokenType.STRING,currString))
                        self.tokens.append(Token(TokenType.QUOTE))

    def getToken(self, char) :
        if char == "\'" or char == "\"" :
            return Token(TokenType.QUOTE)
        elif char == "(" :
            return Token(TokenType.LPAREN)
        elif char == ")" :
            return Token(TokenType.RPAREN)
        
                
    def isToken(self, char) :
        if char == " " or char == "\n" :
            return False
        return True


        
