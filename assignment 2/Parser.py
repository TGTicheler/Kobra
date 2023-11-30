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

    def printTree(self):
        if(self.token.type == Token.VAR):
            print(self.token.var, end="")
            return

        print("(", end="")

        if (self.token.type == Token.LAMBDA):
            print(f"{self.token.var}", end="")
            self.left.printTree()
            print(" ", end="")
            self.right.printTree()
        elif (self.token.type == Token.APPL):
            self.left.printTree()
            print(" ", end="")
            self.right.printTree()

        print(")", end="")

class Pars:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.lhaakjes = 0
        self.root = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
        
    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    def getRoot(self):
        return self.root
        
    def pExpr(self):
        tok = self.current_tok
        if(self.lhaakjes == 0 and tok.type == Token.RPAR):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
        elif(tok.type == Token.VAR):
            return True, Node(Token.Token(Token.VAR, tok.var))
        elif(tok.type == Token.LPAR):
            self.lhaakjes += 1
            node = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
            tok = self.current_tok
            if(tok.type == Token.RPAR):
                self.lhaakjes -= 1
                return True, node
            else:
                print(f"Syntax error: right bracket not found after an opening left bracket.")
                exit(1)

        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
        
    def lExpr(self, passed):
        self.advance()
        tok = self.current_tok
        juist, temp = self.pExpr()
        if(self.lhaakjes == 0 and tok.type == Token.RPAR):
            exit(0)
        elif(juist == True):
            if(passed.token.type == Token.EMPTY):
                node = temp
            else:
                appl = Node(Token.Token(Token.APPL, "@"))
                appl.left = passed
                appl.right = temp
                node = appl
            return True, node
        elif(tok.type == Token.LAMBDA):
            self.advance()
            lamb = Node(Token.Token(Token.LAMBDA, "\\"))
            tok = self.current_tok
            if(tok.type == Token.VAR):
                lamb.left = Node(Token.Token(Token.VAR, tok.var))
                juist, lamb.right = self.lExpr(Node(Token.Token(Token.EMPTY, "EMPTY")))
                if(juist == False):
                    print(f"Syntax error: left expresssion not found.")
                    exit(1)
                elif(passed.token.type == Token.EMPTY):
                    node = lamb
                else:
                    appl = Node(Token.Token(Token.APPL, "@"))
                    appl.left = passed
                    appl.right = lamb
                    node = appl
                return True, node
            else:
                print(f"Syntax error: no variable found after \\")
                exit(1)
        
        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
    
    def dashExpr(self, passed):
        juist, temp = self.lExpr(passed)
        if(juist == True):
            node = self.dashExpr(temp)
            return node
        return passed

    def expr(self, passed):
        juist, temp = self.lExpr(passed)
        if (juist == False):
            print(f"Syntax error: wrong input.")
            exit(1)
        node = self.dashExpr(temp)
        return node
    
def connectFamily(node):
    if node.left != None:
        node.left.parent = node
        node.left = connectFamily(node.left)

    if node.right != None:
        node.right.parent = node
        node.right = connectFamily(node.right)

    return node