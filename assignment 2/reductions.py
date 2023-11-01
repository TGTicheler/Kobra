# Paul Tielens s3612031
# Thom Ticheler s3696820
# Laura Faas s3443159
# Concepts of Programming Languages, 2023

import Token
import Parser
import string

class reduce:
    def __init__(self, root):
        self.max = 1000
        self.current = 0
        self.root = root

    def run(self):
        reduced = self.seekBeta(self.root)
        if(self.current >= self.max):
            print(f"Meer dan {self.max} Beta reductions uitgevoerd, expressie reduceren wordt gestopt.")
            print("Uiteindelijke expressie: ")
        self.current = 0
        reduced.stringTeruggeven()
        print()
        return reduced

    def makeVar(self, vars):
        for i in range(len(string.ascii_letters)):
            if(string.ascii_letters[i] not in vars):
                return string.ascii_letters[i]
            
    def collectVars(self, node, vars):
        if(self.current > self.max ):
            return
        elif(node.token.type== Token.VAR):
            if(node.token.var not in vars):
                vars.append(node.token.var)
        else:
            self.collectVars(node.left, vars)
            self.collectVars(node.right, vars)
    
    def alphaCon(self, node, oldVars, subVars, Nvars):
        if(self.current > self.max ):
            return node
        elif(node.token.type== Token.VAR):
            for i in range(len(oldVars)-1, -1, -1):
                if (oldVars[i] == node.token.var):
                    node.token.var = subVars[i]
                    return node
        elif(node.token.type== Token.LAMBDA):
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
        if(self.current > self.max  ):
            return node
        elif(node.token.type== Token.VAR):
            if(node.token.var == old):
                node = new
        else:
            node.left = self.replaceNode(node.left, old, new)
            node.right = self.replaceNode(node.right, old, new)

        return node

    def betaRed(self, node):
        if(self.current > self.max  ):
            return node
        elif(node.token.type== Token.APPL):
            if(node.left.token.type== Token.LAMBDA):
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
        if (self.current > self.max ):
            return node
        elif (node.token.type== Token.APPL):
            if(node.left.token.type== Token.LAMBDA):
                self.current += 1
                node = self.betaRed(node)
                if(self.current <= self.max):
                    node = self.seekBeta(node)
                return node
        
        if(node.left != None):
            node.left = self.seekBeta(node.left)
        if(node.right != None):
            node.right = self.seekBeta(node.right)

        return node            


