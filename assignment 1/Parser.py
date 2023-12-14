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

# the nodes which the ast is built from
class Node:
    def __init__(self, token):
        self.left = None
        self.right = None
        self.token = token

    def __repr__(self):
        if self.type == Token.VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'

    # prints, from the token, the tree in pre-order
    # used for testing
    def printPreOrder(self):
        print(self.token.var, " ", end= "")

        if self.left:
            self.left.printPreOrder()

        if self.right:
            self.right.printPreOrder()

    # prints the expression from the tree
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

# builds an ast from an array of tokens
class Pars:
    # constructor
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokensIndex = -1 # index of current token in the array
        # amount of left parentheses minus amount of right parentheses
        # can never be < 0
        self.lparentheses = 0 
        # recursive descent for parsing is started
        self.root = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
    
    # advances to the next token in the array
    def advance(self):
        if self.tokensIndex < len(self.tokens):
            self.tokensIndex += 1
            self.currentToken = self.tokens[self.tokensIndex]
        return self.currentToken
    
    # gives the root of the ast
    def getRoot(self):
        return self.root

    # The LL grammar that is used:
    # ⟨expr⟩ ::= ⟨lexpr⟩ ⟨expr'⟩
    # ⟨expr'⟩ ::= ⟨lexpr⟩ ⟨expr'⟩ | Empty
    # ⟨lexpr⟩ ::= ⟨pexpr⟩ | '\' ⟨var⟩ ⟨lexpr⟩
    # ⟨pexpr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')'

    # the next functions below are used to implement this LL grammar

    # checks if current token is a variable or '(' ⟨expr⟩ ')'
    # and returns a node of a variable or the node of the root of the expression    
    def pExpr(self):
        tok = self.currentToken
        if(self.lparentheses == 0 and tok.type == Token.RPAR):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
        elif(tok.type == Token.VAR):
            return True, Node(Token.Token(Token.VAR, tok.var))
        elif(tok.type == Token.LPAR):
            self.lparentheses += 1
            node = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")))
            tok = self.currentToken
            if(tok.type == Token.RPAR):
                self.lparentheses -= 1
                return True, node
            else:
                print(f"Syntax error: right bracket not found after an opening left bracket.")
                exit(1)

        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))

    # checks if current token is a pexpr or an abstraction
    # returns the corresponding sub abstract syntax tree
    # "leftChild" is used to make applications left-associative
    def lExpr(self, leftChild):
        self.advance()
        tok = self.currentToken
        correct, temp = self.pExpr()
        # if there is a right paranthesis whithout any left parentheses left
        if(self.lparentheses == 0 and tok.type == Token.RPAR):
            print(f"Syntax error: right paranthesis found without an opening left paranthesis. 2")
            print("exit status 1")
            exit(1)
        elif(correct == True):
            # "leftChild" is used here to make applications left-associative
            if(leftChild.token.type == Token.EMPTY):
                node = temp
            else:
                # making and returning an application
                appl = Node(Token.Token(Token.APPL, "@"))
                appl.left = leftChild
                appl.right = temp
                node = appl
            return True, node
        elif(tok.type == Token.LAMBDA):
            self.advance()
            # making and returning an abstraction
            lamb = Node(Token.Token(Token.LAMBDA, "\\"))
            tok = self.currentToken
            if(tok.type == Token.VAR):
                lamb.left = Node(Token.Token(Token.VAR, tok.var))
                # checking if it has an expression
                correct, lamb.right = self.lExpr(Node(Token.Token(Token.EMPTY, "EMPTY")))
                if(correct == False):
                    print(f"Syntax error: left expresssion not found.")
                    exit(1)
                elif(leftChild.token.type == Token.EMPTY):
                    node = lamb
                else:
                    # "leftChild" is used here to make applications left-associative
                    appl = Node(Token.Token(Token.APPL, "@"))
                    appl.left = leftChild
                    appl.right = lamb
                    node = appl
                return True, node
            else:
                print(f"Syntax error: no variable found after \\")
                exit(1)
        
        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))

    # checks if current token is a lexpr if so 
    # returns the corresponding sub abstract syntax tree
    # if not nothing happens
    # "leftChild" is used to make applications left-associative    
    def exprApo(self, passed):
        juist, passFurther = self.lExpr(passed)
        if(juist == True):
            node = self.exprApo(passFurther)
            return node
        return passed

    # checks if current token is a lexpr if so 
    # returns the corresponding sub abstract syntax tree
    # if not then error is thrown
    # "leftChild" is used to make applications left-associative
    def expr(self, passed):
        juist, passFurther = self.lExpr(passed)
        if (juist == False):
            print(f"Syntax error: wrong input.")
            exit(1)
        node = self.exprApo(passFurther)
        return node
    