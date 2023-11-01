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
        if self.token.type == Token.LVAR or self.token.type == Token.UVAR:
            return f'{self.type}:{self.var}'
        return f'{self.token.type}'

    #pre-order
    def printPreOrder(self):
        print(self.token.var, " ", end= "")

        if self.left:
            self.left.printPreOrder()

        if self.right:
            self.right.printPreOrder()

    def stringTeruggeven(self):
        if(self.token.type == Token.LVAR or self.token.type == Token.UVAR):
            print(self.token.var, end="")
            return
        elif(self.token.type == Token.COLON):
            self.left.stringTeruggeven()
            print(":", end="")
            self.right.stringTeruggeven()
            return


        print("(", end="")

        if (self.token.type == Token.LAMBDA):
            print(f"{self.token.var}", end="")
            self.left.stringTeruggeven()
            print("^", end="")
            self.left.left.stringTeruggeven()
            print(" ", end= "")
            self.right.stringTeruggeven()
        elif (self.token.type == Token.APPL):
            self.left.stringTeruggeven()
            print(" ", end="")
            self.right.stringTeruggeven()
        elif (self.token.type == Token.TO):
            self.left.stringTeruggeven()
            print(f"{self.token.var}", end="")
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
    
    def back(self):
        if self.tok_idx > 0:
            self.tok_idx -= 1
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        self.root = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
        tok = self.current_tok
        if(tok.type != Token.COLON):
            print("Syntax error: missing ':'.")
            exit(1)
        colon = Node(Token.Token(Token.COLON, ":"))
        colon.left = self.root
        juist, colon.right = self.Type()
        if(juist == False):
            print("Error: missing type.")
            print("exit status 1")
            exit(1)
        self.root = colon
        self.root = connectFamily(self.root)
        kVars = []
        uVars =[]
        self.seekUnkownType(self.root.left, kVars, uVars)
        if (uVars != []):
            print(f"Error: {uVars} have unkown types.")
            print("exit status 1")
            exit(1)
        return self.root
        
    def pExpr(self):
        tok = self.current_tok
        if(self.lhaakjes == 0 and tok.type == Token.RHAAK):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
        elif(tok.type == Token.LVAR):
            return True, Node(Token.Token(Token.LVAR, tok.var))
        elif(tok.type == Token.LHAAK):
            self.lhaakjes += 1
            node = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
            tok = self.current_tok
            if(tok.type == Token.RHAAK):
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
        if(self.lhaakjes == 0 and tok.type == Token.RHAAK):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
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
            if(tok.type == Token.LVAR):
                lamb.left = Node(Token.Token(Token.LVAR, tok.var))
                self.advance()
                tok = self.current_tok
                if(tok.type != Token.CIRCUMFLEX):
                    print("Syntax error: missing '^'.")
                    print("exit status 1")
                    exit(1)
                juist, circumflex = self.Type()
                if(juist == False):
                    print("Syntax error: missing type in abstraction.")
                    print("exit status 1")
                    exit(1)
                lamb.left.left = circumflex
                self.back()
                juist, lamb.right = self.lExpr(Node(Token.Token(Token.EMPTY, "EMPTY")))
                if(juist == False):
                    print(self.current_tok)
                    print(f"Syntax error: expresssion in abstraction not found.")
                    print("exit status 1")
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
    

    def Type(self):
        self.advance()
        tok = self.current_tok
        if(tok.type == Token.UVAR):
            nietLeeg, right = self.TypePrime()
            node = Node(Token.Token(Token.UVAR, tok.var))
            if(nietLeeg == True):
                to = Node(Token.Token(Token.TO, "->"))
                to.left = node
                to.right = right
                node = to
            return True, node
        elif(tok.type == Token.LHAAK):
            juist, node = self.Type()
            if(juist == True):
                tok = self.current_tok
                if(tok.type != Token.RHAAK):
                    print(f"Syntax error: right bracket not found after an opening left bracket.")
                    print("exit status 1")
                    exit(1)
                
                nietLeeg, right = self.TypePrime()
                if(nietLeeg == True):
                    to = Node(Token.Token(Token.TO, "->"))
                    to.left = node
                    to.right = right
                    node = to
                return True, node
            else:
                print(f"Syntax error: incorrect type.")
                print("exit status 1")
                exit(1)
        else:
            return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
            

    def TypePrime(self):
        self.advance()
        tok = self.current_tok
        if(tok.type == Token.TO):
            juist, node = self.Type()
            if(juist == True):
                return True, node
            else:
                print(f"Syntax error: incorrect type.")
                print("exit status 1")
                exit(1)
        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))

    
    def seekUnkownType(self, node, kVars, Uvars):
        if(node.token.type == Token.LAMBDA and node.left.token.var not in kVars):
            kVars.append(node.left.token.var)
        elif(node.token.var not in kVars and node.token.type == Token.LVAR and node.token.var not in Uvars):
            Uvars.append(node.token.var)
        
        if(node.left != None):
            self.seekUnkownType(node.left, kVars, Uvars)
        if(node.right != None):
            self.seekUnkownType(node.right, kVars, Uvars)


def connectFamily(node):
    if node.left != None:
        node.left.parent = node
        node.left = connectFamily(node.left)

    if node.right != None:
        node.right.parent = node
        node.right = connectFamily(node.right)

    return node