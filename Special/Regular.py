# Regular -- Parse tree node strategy for printing regular lists

from Special import Special
import sys

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        if(p):
            if(n >= 0):
                sys.stdout.write(" ")
                sys.stdout.flush()
            else:
                sys.stdout.write("")
                sys.stdout.flush()
        else:
            sys.stdout.write("(")
            sys.stdout.flush()
        t.car.print(n,not t.car.isPair())
        if(t.cdr.isPair()):
            t.cdr.print(n,True)
        elif(t.cdr.isNull()):
            sys.stdout.write(")")
            sys.stdout.flush()
        else:
            t.cdr.print(n,True)
            sys.stdout.write(")")
            sys.stdout.flush()
