# Paul Tielens s3612031
# Thom Ticheler s3696820
# Laura Faas s3443159
# Concepts of Programming Languages, 2023

# Parses an array of tokens of lambda calculus and makes a binary tree

import Token

class Node:
    def __init__(self, token):
        self.left = None
        self.right = None
        self.token = token
        self.parent = None

    def __repr__(self):
        if self.type == Token.VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'

    #pre-order
    def printPreOrder(self):
        print(self.token.var, " ", end= "")

        if self.left:
            self.left.printPreOrder()

        if self.right:
            self.right.printPreOrder()
    

    def stringTeruggeven(self):
        if(self.token.type == Token.VAR):
            print(self.token.var, end="")
            return

        print("(", end="")

        if (self.token.type == Token.LAMBDA):
            print(f"{self.token.var}", end="")
            self.left.stringTeruggeven()
            print(" ", end="")
            self.right.stringTeruggeven()
        elif (self.token.type == Token.APPL):
            self.left.stringTeruggeven()
            print(" ", end="")
            self.right.stringTeruggeven()

        print(")", end="")




class Pars:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.lhaakjes = 0
        self.root = None


    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        juist, self.root = self.expr()
        self.root = connectFamily(self.root)
        self.root.stringTeruggeven()
        print()
        return self.root


        


    def pExpr(self):
        tok = self.current_tok
        if(self.lhaakjes == 0 and tok.type == Token.RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit(0)
        elif(tok.type == Token.VAR):
            return True, Node(Token.Token(Token.VAR, tok.var))
        elif(tok.type == Token.LHAAK):
            self.lhaakjes += 1
            juist, node = self.expr()
            if(juist == True):
                tok = self.current_tok
                if(tok.type == Token.RHAAK):
                    self.lhaakjes -= 1
                    return True, node
                else:
                    print('ERROR geen Rhaakje --------------')
                    exit(0)
            else:
                print('ERROR geen expressie in ( )---------------')
                exit(0)

        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
        
    def lExpr(self):
        self.advance()
        tok = self.current_tok
        juist, node = self.pExpr()
        if(self.lhaakjes == 0 and tok.type == Token.RHAAK):
            exit(0)
        elif(juist == True):
            return True, node
        elif(tok.type == Token.LAMBDA):
            self.advance()
            node = Node(Token.Token(Token.LAMBDA, "\\"))
            tok = self.current_tok
            if(tok.type == Token.VAR):
                node.left = Node(Token.Token(Token.VAR, tok.var))
                juist, node.right = self.lExpr()
                if(juist == False):
                    print('ERROR mist lExpr-------------')
                    exit(0)
                return True, node
            else:
                print('ERROR geen variabele bij Lambda-----------------')
                exit(0)
        
        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
    
    def dashExpr(self):
        juist, left = self.lExpr()
        if(juist == True):
            nietLeeg, right = self.dashExpr()
            if(nietLeeg == True):
                node = Node(Token.Token(Token.APPL, "@"))
                node.left = left
                node.right = right
            else:
                node = left
            return True, node
        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))

    def expr(self):
        juist, left = self.lExpr()
        if (juist == False):
            print("Onjuiste invoer")
            exit(0)
        nietLeeg, right = self.dashExpr()
        if(nietLeeg == True):
            node = Node(Token.Token(Token.APPL, "@"))
            node.left = left
            node.right = right
        else:
            node = left
        return True, node
    
def connectFamily(node):
    if (node.left != None):
        node.left.parent = node
        node.left = connectFamily(node.left)

    if (node.right != None):
        node.right.parent = node
        node.right = connectFamily(node.right)

    return node
