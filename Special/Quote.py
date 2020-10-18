# Quote -- Parse tree node strategy for printing the special form quote

from Special import Special
import sys

class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p, newLine = False):        
        if(t.cdr.isPair()):
            t.cdr.print(n,False)
        elif(t.cdr.isNull()):
            t.cdr.print(n,True)
            #sys.stdout.write(")")
            #sys.stdout.flush()
        else:
            sys.stdout.write(" . ")
            t.cdr.print(n,True)
            sys.stdout.write(")")
            sys.stdout.flush()
