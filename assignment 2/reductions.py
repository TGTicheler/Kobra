#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 
# Paul Tielens s3612031
# Thom Ticheler s3696820
# Laura Faas s3443159
# Concepts of Programming Languages, 2023

# performs beta-reductions and alpha-conversions on an ast

import Token
import string

# makes a reduced ast from an ast
class reduce:
    def __init__(self, root):
        self.maxRed = 1000 # maximum number of reduction steps
        self.currentRed = 0 # current amount of reduction steps
        self.root = root
        # recursively looks through the ast for beta-reductions
        # outputs a reduced ast
        try:
            self.reduced = self.seekBeta(self.root)
        except:
            print("Too many reduction steps performed")
            print("exit status 1")
            exit(1)

    # gives the root of the reduced ast
    def getReducedTree(self):
        return self.reduced

    # takes in an array of strings and produces a one letter variable 
    # that is not in the array
    def makeVar(self, vars):
        for i in range(len(string.ascii_letters)):
            if(string.ascii_letters[i] not in vars):
                return string.ascii_letters[i]

    # collects all of the variables in an ast and adds it to "vars"       
    def collectVars(self, node, vars):
        if(self.currentRed > self.maxRed ):
            return
        elif(node.token.type == Token.VAR):
            if(node.token.var not in vars):
                vars.append(node.token.var)
        else:
            self.collectVars(node.left, vars)
            self.collectVars(node.right, vars)

    # for the functions below we use
    # ((\x M) N) when reduced becomes:
    # M[x:=N]
    
    # if there are free/bound variables in N that are bound in M
    # then the alphaconversion is needed


    # looks through a sub ast if there any variables in N (Nvars) bound in M
    # if so these variables in M are changed and also their bound variables
    # the variables that are changed are kept in oldVars 
    # and what they are changed to is kept in subVars
    # if there is a bound variable bound again then the subVar will be changed
    # example: (\x (x (\x x))) becomes (\a (a (\b b)))
    def alphaCon(self, node, oldVars, subVars, Nvars):
        if(self.currentRed > self.maxRed ):
            return node
        elif(node.token.type == Token.VAR):
            # checks from the latest changed vars if the current var needs to be changed
            for i in range(len(oldVars)-1, -1, -1):
                if (oldVars[i] == node.token.var):
                    node.token.var = subVars[i]
                    return node
        elif(node.token.type == Token.LAMBDA):
            # checks if there is a variable in N that is bound here
            if(node.left.token.var in Nvars):
                oldVars.append(node.left.token.var)
                vars = Nvars + subVars 
                self.collectVars(node.right,vars) # the new variable cannot have already been used
                newVar = self.makeVar(vars)
                if(newVar == None):
                    print("Too many variables, could not make a new variable")
                    print("exit status 1")
                    exit(1)
                subVars.append(newVar)
                node.left.token.var = newVar
                node.right = self.alphaCon(node.right, oldVars, subVars, Nvars)
                return node

        # so it goes through the whole ast
        if(node.left != None):    
            node.left = self.alphaCon(node.left, oldVars, subVars, Nvars)
        if(node.right != None):
            node.right = self.alphaCon(node.right, oldVars, subVars, Nvars)
        return node


    # looks recursively for the variable "old" to be replaced with the sub ast "new" 
    def replaceNode(self, node, old, new):
        if(self.currentRed > self.maxRed  ):
            return node
        elif(node.token.type == Token.VAR):
            if(node.token.var == old):
                node = new
        else:
            node.left = self.replaceNode(node.left, old, new)
            node.right = self.replaceNode(node.right, old, new)

        return node

    def betaRed(self, node):
        if(self.currentRed > self.maxRed  ):
            return node
        elif(node.token.type == Token.APPL):
            if(node.left.token.type == Token.LAMBDA):
                node.parent = None
                N = node.right
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

    def seekBeta(self, node):
        if (self.currentRed > self.maxRed ):
            return node
        elif (node.token.type == Token.APPL):
            if(node.left.token.type == Token.LAMBDA):
                self.currentRed += 1
                node = self.betaRed(node)
                if(self.currentRed <= self.maxRed):
                    node = self.seekBeta(node)
                return node
        
        if(node.left != None):
            node.left = self.seekBeta(node.left)
        if(node.right != None):
            node.right = self.seekBeta(node.right)

        return node            


