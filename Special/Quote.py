# Quote -- Parse tree node strategy for printing the special form quote

from Special import Special
import sys

class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass
       
    def print(self, t, n, parenPrinted, newLine = False):
        if(newLine):
            sys.stdout.write("\n")
            sys.stdout.flush()
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write("\'")
        sys.stdout.flush()
        if(t.cdr.isPair()):            
            t.cdr.print(n,False)
        elif(t.cdr.isNull()):
            t.cdr.print(n,False)
        else:
            t.cdr.print(n,True)

