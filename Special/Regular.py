# Regular -- Parse tree node strategy for printing regular lists

from Special import Special
import sys

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p, newLine = False):
        if(p):
            if(not newLine):
                sys.stdout.write(" ")
                sys.stdout.flush()
            else:
                sys.stdout.write("\n")
                sys.stdout.flush()
        else:
            sys.stdout.write("(")
            sys.stdout.flush()
        t.car.print(n,not t.car.isPair())
        if(t.cdr.isPair()):            
            t.cdr.print(n,True)
        elif(t.cdr.isNull()):
            t.cdr.print(n,True)
            #sys.stdout.write(")")
            #sys.stdout.flush()
        else:
            sys.stdout.write(" . ")
            t.cdr.print(n,True)
            sys.stdout.write(")")
            sys.stdout.flush()
