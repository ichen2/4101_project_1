# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *

class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch
    
    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            # TODO: Skip white space and comments

            # Return None on EOF
            if ch == "":
                return None

            # Skip empty space
            elif ch == "\n" or ch == " ":
                return self.getNextToken()

            # Skip comments 
            elif ch == ";":                
                while(not ch == "\n"):
                    ch = self.read()
                return self.getNextToken()
                
            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '\"':
                self.buf = []
                while self.peek() != "\"":
                    self.buf += self.read()
                self.ch_buf = None
                return StrToken("".join(self.buf))

            # Identifiers
            elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or ch == '!' or ch == '$' or ch ==  '%' or ch ==  '&' or ch == '*' or ch =='+' or ch == '-' or ch == '.' or ch == '/' or ch == ':' or ch == '<' or ch ==  '=' or ch == '>' or ch == '?' or ch == '@' or ch == '^'  or ch == '_' or ch == '~' :
                # or ch is some other vaid first character
                # for an identifier
                self.buf = [ch]
                p = self.peek()
                while (p >= '0' and p <= '9' ) or (p >= 'A' and p <= 'Z') or (p >= 'a' and p <= 'z') or p == '!' or p == '$' or p ==  '%' or p ==  '&' or p == '*' or p =='+' or p == '-' or p == '.' or p == '/' or p == ':' or p == '<' or p ==  '=' or p == '>' or p == '?' or p == '@' or p == '^'  or p == '_' or p == '~' :
                    self.buf += self.read()
                    p = self.peek()
                # make sure that the character following the identifier
                # is not removed from the input stream
                return IdentToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')
                while self.isDigit(self.peek()):
                    i = i * 10
                    i +=  ord(self.read()) - ord('0')
                return IntToken(i)

            # Illegal character
            else:
                print("end")
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
