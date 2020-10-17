# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident
# gerald said to import these
from Special import *

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):
        if(self.car.isSymbol()):
            t = self.car.getName()
            if(t == "\'"):
                self.form = Quote()
            elif(t == "quote"):
                self.form = Quote()
            elif(t == "lambda"):
                self.form = Lambda()
            elif(t == "begin"):
                self.form = Begin()
            elif(t == "if"):
                self.form = If()
            elif(t == "let"):
                self.form = Let()
            elif(t == "cond"):
                self.form = Cond()
            elif(t == "define"):
                self.form = Define()
            elif(t == "set!"):
                self.form = Set()
            else:
                self.form = Regular()
        else:
            self.form = Regular()

    def print(self, n, p=False):
        self.form.print(self, n, p)
    
    def simplePrint(self):
        self.car.simplePrint()
        print(self.form)
        self.cdr.simplePrint()

    def isPair(self):           
        return True

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
