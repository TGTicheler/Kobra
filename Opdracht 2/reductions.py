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

    def makeVar(vars):
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
    

    #krijgt de node met de Lambda in
    def alphaCon(self, node):
        if(node.token.soort == LAMBDA):
            print("lets go")
        else:
            print("ERROR: geen lambda in de node")
            exit(0)


vars = []
root = Parser.Node(Token.Token(LAMBDA, "\\"))
root.left = Parser.Node(Token.Token(VAR, "a"))
root.right = Parser.Node(Token.Token(VAR, "a"))
test = reduce()
test.collectVars(root, vars)
print(vars)