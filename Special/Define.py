# Define -- Parse tree node strategy for printing the special form define

from Special import Special
import sys

class Define(Special):
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
        if(t.cdr.car.isPair()):
            t.cdr.car.print(n, False)
            sys.stdout.write("\n")
            sys.stdout.flush()
            t.cdr.cdr.car.print(n+4, False)
            sys.stdout.write("\n")
            sys.stdout.flush()
        # if(t.cdr.isPair()):
        #     t.cdr.print(n,True)
        # elif(t.cdr.isNull()):
        #     t.cdr.print(n,True)
        #     #sys.stdout.write(")")
        #     #sys.stdout.flush()
        # else:
        #     sys.stdout.write(" . ")
        #     t.cdr.print(n,True)
        #     sys.stdout.write(")")
        #     sys.stdout.flush()
