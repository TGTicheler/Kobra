import Token
import Parser
import string

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

class reduce:
    def __init__(self):
        self.max = 1000

    def makeVar(self, vars):
        for i in range(len(string.ascii_letters)):
            if(string.ascii_letters[i] not in vars):
                return string.ascii_letters[i]
            
    def collectVars(self, node, vars):
        if(node.token.soort == VAR):
            if(node.token.var not in vars):
                vars.append(node.token.var)
        else:
            self.collectVars(node.left, vars)
            self.collectVars(node.right, vars)

    def changeVars(self, node, oldVar, nwVar):
        if(node.token.soort == VAR):
            if(node.token.var == oldVar):
                node.token.var = nwVar
        else:
            node.left = self.changeVars(node.left, oldVar, nwVar)
            node.left = self.changeVars(node.right, oldVar, nwVar)
        return node
    

    #krijgt de node met de Lambda in
    def alphaCon(self, node):
        if(node.token.soort == LAMBDA):
            vars = []
            self.collectVars(node, vars)
            nwVar = self.makeVar(vars)
            node = self.changeVars(node, node.left.token.var, nwVar)
            return node
        else:
            print("ERROR: geen lambda in de node")
            exit(0)


vars = []
root = Parser.Node(Token.Token(LAMBDA, "\\"))
root.left = Parser.Node(Token.Token(VAR, "a"))
root.right = Parser.Node(Token.Token(VAR, "a"))
test = reduce()
root = test.alphaCon(root)
root.printPreOrder()
print()