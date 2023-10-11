LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

class Token:
    def __init__(self, soort, var=None):
        self.soort = soort
        self.var = var

    def __repr__(self):
        if self.var:
            return f'{self.soort}:{self.var}'
        return f'{self.soort}'

class biNode:
    def __init__(self, data, var):
        self.left = None
        self.right = None
        self.data = data
        self.var = var
        self.parent = None

    def __repr__(self):
        self.PrintTree()


    def PrintTree(self):
        print(self.var)

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()
                
class varNode:
    def __init__(self, var):
        self.var = var
        self.parent = None
    
    def __repr__(self):
        print(self.var)

    def PrintTree(self):
        print(self.var)


def test():
    root = biNode(Token(LAMBDA), "\\")
    root.left = varNode("Paul")
    root.right = biNode(Token(APPL), "@")
    test = root.right
    test.left = varNode("knap")
    test.right = varNode("geweldig")
    root.right = None
    return root

def test2():
    lol = varNode("aub")
    lol = biNode(Token(EMPTY),"verandert")
    lol.left = varNode("lol is mijn papa")
    lol.right = varNode("ook die van mij")
    return True, lol
# root = test()
# root = test2(root)
# root.PrintTree()

root = biNode(Token(APPL), "akdj")
root.left = varNode("no me gusta")

juist, root.right = test2()
if(juist == True):
    print("we take those")
root.PrintTree()
