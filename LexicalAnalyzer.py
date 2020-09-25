from Tokens import *

class LexicalAnalyzer :
    def __init__( self, fileName ) :
        self.inFile = file(fileName, 'r')
    def nextLine(self) :
        return self.inFile.readLine()
        
