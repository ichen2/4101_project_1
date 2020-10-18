# Define -- Parse tree node strategy for printing the special form define

from Special import Special
import sys

class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, parenPrinted, newLine = False):
        isVar = True
        if(newLine):
            sys.stdout.write("\n")
            sys.stdout.flush()
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write("(define ")
        sys.stdout.flush()
        if(t.cdr.car.isPair()):
            isVar = False
        t.cdr.car.print(n, False)
        if(isVar):
            sys.stdout.write(" ")
            sys.stdout.flush()
            t.cdr.cdr.car.print(n,True)
        else:
            if(t.cdr.cdr.car.isPair()):
                t.cdr.cdr.car.print(n+4,False,True)
            else:  
                sys.stdout.write("\n")
                sys.stdout.flush()
                for _ in range(n+4):
                    sys.stdout.write(' ')
                t.cdr.cdr.car.print(n+4,False,True)
        if(not isVar):
            sys.stdout.write("\n")
            for _ in range(n):
                sys.stdout.write(' ')
        sys.stdout.write(")")
        sys.stdout.flush()
        
