# Lambda -- Parse tree node strategy for printing the special form lambda

from Special import Special
import sys

class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, parenPrinted, newLine = False):
        if(newLine):
            sys.stdout.write("\n")
            sys.stdout.flush()
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write("(lambda ")
        sys.stdout.flush()
        t.cdr.car.print(n, False)
        if(t.cdr.cdr.car.isPair()):
            t.cdr.cdr.car.print(n+4,False,True)
        else:  
            sys.stdout.write("\n")
            sys.stdout.flush()
            for _ in range(n+4):
                sys.stdout.write(' ')
            t.cdr.cdr.car.print(n+4,False,True)
        sys.stdout.write("\n")
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write(")")
        sys.stdout.flush()
