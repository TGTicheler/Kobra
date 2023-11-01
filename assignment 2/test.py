import string

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
        
def makeVar(vars):
    for i in range(len(string.ascii_letters)):
        if(string.ascii_letters[i] not in vars):
            return string.ascii_letters[i]
        
def collectVars(node, vars):
    if(node.token.soort == VAR):
        vars.append(node.token.var)
    else:
        if node.left.token.soort == VAR:
            vars.append(node.left.token.var)
        else:
            collectVars(node.left, vars)

        if node.right.token.soort == VAR:
            vars.append(node.right.token.var)
        else:
            collectVars(node.right, vars)


# root = Node(Token(APPL, '@'))
# root.left = Node(Token(VAR, "eerste"))
# root.right = Node(Token(LAMBDA, "\\"))
# root.right.left = Node(Token(VAR, "tweede"))
# root.right.right = Node(Token(VAR, "laatste"))
# root.printPreOrder()
# root.left.token.var = "verandert lets go"
# print("-----------------")
# root.printPreOrder()

# root.printPreOrder()
# print("---------------------")
# root.left.printPreOrder()
# print("-------------------")
# root.right.printPreOrder()
# print("-------------------")


# root = connectFamily(root)
# root.left.parent.printPreOrder()
# print("-------------------")
# root.right.right.parent.printPreOrder()
# print("-------------------")
# root.right.right.parent.parent.printPreOrder()
# print("-------------------")

# vars = []

# collectVars(root, vars)
# print(vars)
lijst = ["a", "b", "c"]

for i in range(len(lijst)-1,-1,-1):
    lijst[i]

