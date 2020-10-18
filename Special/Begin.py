# Begin -- Parse tree node strategy for printing the special form begin

from Special import Special
import sys

class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, parenPrinted, newLine = False):
        if(newLine):
            sys.stdout.write("\n")
            sys.stdout.flush()
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write("(begin ")
        sys.stdout.flush()
        while(not t.cdr.isNull()):
            if(t.cdr.car.isPair()):
                t.cdr.car.print(n+4,False,True)
            else:
                sys.stdout.write("\n")
                sys.stdout.flush()
                for _ in range(n+4):
                    sys.stdout.write(' ')
                t.cdr.car.print(n+4,False,True)
            t = t.cdr
        sys.stdout.write("\n")
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write(")")
        sys.stdout.flush()

        