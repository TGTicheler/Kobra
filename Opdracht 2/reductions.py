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
    def __init__(self, root):
        self.max = 1000
        self.root = root

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
    
    #LET OP vergeet niet var buiten alphacon te veranderen
    #krijgt de node met de expr van de lambda in
    def alphaCon(self, node, oldVars, subVars, Nvars):
        if(node.token.soort == VAR):
            for i in range(len(oldVars)-1, -1, -1):
                if (oldVars[i] == node.token.var):
                    node.token.var = subVars[i]
                    return node
        elif(node.token.soort == LAMBDA):
            if(node.left.token.var in Nvars):
                oldVars.append(node.left.token.var)
                vars = Nvars + subVars
                self.collectVars(node.right,vars)
                new = self.makeVar(vars)
                subVars.append(new)
                node.left.token.var = new
                node.right = self.alphaCon(node.right, oldVars, subVars, Nvars)
                return node
        if(node.left != None):    
            node.left = self.alphaCon(node.left, oldVars, subVars, Nvars)
        if(node.right != None):
            node.right = self.alphaCon(node.right, oldVars, subVars, Nvars)
        return node



    def replaceNode(self, node, old, new):
        if(node.token.soort == VAR):
            if(node.token.var == old):
                node = new
        else:
            node.left = self.replaceNode(node.left, old, new)
            node.right = self.replaceNode(node.right, old, new)

        return node

    def betaRed(self, node):
        if(node.token.soort == APPL):
            if(node.left.token.soort == LAMBDA):
                node.parent = None
                N = node.right
                #kijkt naar de vars in N, let op
                Nvars = []
                self.collectVars(N, Nvars)
                oldVars =[]
                newVars = []
                node.left = self.alphaCon(node.left, oldVars, newVars, Nvars)
                var = node.left.left.token.var
                M = node.left.right
                M = self.replaceNode(M, var, N)
                return M
            else:
                print("Onjuist voor beta reduction")
        else:
            print("onjuist voor beta reduction")

        return node



# vars = []
# root = Parser.Node(Token.Token(APPL, "@"))

# root.left = Parser.Node(Token.Token(LAMBDA, "\\"))
# root.right = Parser.Node(Token.Token(APPL, "@"))

# root.right.left = Parser.Node(Token.Token(VAR, "kam aan"))
# root.right.right = Parser.Node(Token.Token(VAR, "je bent er bijna"))

# root.left.left = Parser.Node(Token.Token(VAR, "x"))
# root.left.right = Parser.Node(Token.Token(APPL, "@"))

# root.left.right.left = Parser.Node(Token.Token(VAR, "x"))
# root.left.right.right = Parser.Node(Token.Token(VAR, "x"))

# root.printPreOrder()
# print()
# print("-------------------------------------")
# test = reduce(root)
# root = test.betaRed(root)
# root.printPreOrder()
# print()