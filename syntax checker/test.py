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
        if self.token.soort == VAR:
            return f'{self.token.soort}:{self.token.var}'
        return f'{self.token.soort}'

    #pre-order
    def printPreOrder(self):
        print(self.token.var, " ")

        if self.left:
            self.left.printPreOrder()

        if self.right:
            self.right.printPreOrder()


def connectFamily(node):
    if node.left != None:
        node.left.parent = node
        node.left = connectFamily(node.left)

    if node.right != None:
        node.right.parent = node
        node.right = connectFamily(node.right)

    return node
        


root = Node(Token(APPL, '@'))
root.left = Node(Token(VAR, "eerste"))
root.right = Node(Token(LAMBDA, "\\"))
root.right.left = Node(Token(VAR, "tweede"))
root.right.right = Node(Token(VAR, "laatste"))

root.printPreOrder()
print("---------------------")
root.left.printPreOrder()
print("-------------------")
root.right.printPreOrder()
print("-------------------")


root = connectFamily(root)
root.left.parent.printPreOrder()
print("-------------------")
root.right.parent.printPreOrder()
print("-------------------")
print(root.right.parent)
print(root.left.parent)




