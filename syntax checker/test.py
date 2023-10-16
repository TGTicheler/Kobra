LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

class Token:
    def __init__(self, soort, var):
        self.soort = soort
        self.var = var

    def __repr__(self):
        if self.soort == VAR:
            return f'{self.soort}:{self.var}'
        return f'{self.soort}'

class Node:
    def __init__(self, token):
        self.left = None
        self.right = None
        self.token = token
        self.parent = None

    def __repr__(self):
        if self.type == VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'

    #pre-order
    def PrintTree(self):
        print(self.token.var, " ")

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()


def connectFamily(node):
    if node.left != None:
        node.left.parent = node
        node.left = connectFamily(node.left)

    if node.right != None:
        node.right.parient = node
        node.right = connectFamily(node.right)

    return node
        


root = Node(Token(APPL, "@"))
root.left = Node(Token(VAR, "iets"))
root = connectFamily(root)



root.left.PrintTree()
print("-------------------")
root.left.parent.PrintTree()
print("--------------")
root.PrintTree()
