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
        if self.token.type == Token.LVAR or self.token.type == Token.UVAR:
            return f'{self.token.type}:{self.token.var}'
        return f'{self.token.type}'

    # prints, from the token, the tree in pre-order
    # used for testing
    def printPreOrder(self):
        print(self.token.var, " ", end= "")

        if self.left:
            self.left.printPreOrder()

        if self.right:
            self.right.printPreOrder()

    # gives a string with only ⟨type⟩ grammar
    def giveTypeInString(self, string):
        if(self.token.type == Token.LVAR or self.token.type == Token.UVAR):
            string += self.token.var
            return string
        
        string += "("

        if (self.token.type == Token.TO):
            string = self.left.giveTypeInString(string)
            string += "->"
            string = self.right.giveTypeInString(string)

        string += ")"
        return string

    # prints the judgement from the tree
    def printTree(self):
        if(self.token.type == Token.LVAR or self.token.type == Token.UVAR):
            print(self.token.var, end="")
            return
        elif(self.token.type == Token.COLON):
            self.left.printTree()
            print(":", end="")
            self.right.printTree()
            return

        print("(", end="")

        if (self.token.type == Token.LAMBDA):
            print(f"{self.token.var}", end="")
            self.left.printTree()
            print("^", end="")
            self.left.left.printTree()
            print(" ", end= "")
            self.right.printTree()
        elif (self.token.type == Token.APPL):
            self.left.printTree()
            print(" ", end="")
            self.right.printTree()
        elif (self.token.type == Token.TO):
            self.left.printTree()
            print(f"{self.token.var}", end="")
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
        # keep track of the type corresponding with the variable
        vars = []
        types = []
        # recursive descent for parsing is started
        self.root = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")), vars, types)
        # adding the type side to the ast        
        tok = self.current_tok
        if(tok.type != Token.COLON):
            print("Syntax error: missing ':'")
            print("exit status 1")
            exit(1)
        colon = Node(Token.Token(Token.COLON, ":"))
        colon.left = self.root # expression is the left side of the ast
        juist, colon.right = self.Type() # type is the right side
        if(juist == False):
            print("Error: missing type.")
            print("exit status 1")
            exit(1)
        self.root = colon

    # advances to the next token in the array
    def advance(self):
        if self.tokensIndex < len(self.tokens):
            self.tokensIndex += 1
            self.current_tok = self.tokens[self.tokensIndex]
        return self.current_tok
    
    # goes back to the previous token in the array
    def back(self):
        if self.tokensIndex > 0:
            self.tokensIndex -= 1
            self.current_tok = self.tokens[self.tokensIndex]
        return self.current_tok

    # gives the root of the ast
    def getRoot(self):
        return self.root
    
    # The LL grammar that is used:
    # ⟨judgement⟩ ::= ⟨expr⟩ ':' ⟨type⟩
    # ⟨expr⟩ ::= ⟨lexpr⟩ ⟨expr'⟩
    # ⟨expr'⟩ ::= ⟨lexpr⟩ ⟨expr'⟩ | Empty
    # ⟨lexpr⟩ ::= ⟨pexpr⟩ | '\' ⟨var⟩ ⟨lexpr⟩
    # ⟨pexpr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')'
    # ⟨type⟩ ::= ⟨uvar⟩ ⟨type'⟩ | '(' ⟨type⟩ ')' ⟨type'⟩ 
    # ⟨type'⟩ ::=  '->' ⟨type⟩ | Empty
        
    # the next functions below are used to implement this LL grammar


    # checks if current token is a variable or '(' ⟨expr⟩ ')'
    # and returns a node of a variable or the node of the root of the expression    
    def pExpr(self, vars, types):
        tok = self.current_tok
        if(self.lparentheses == 0 and tok.type == Token.RHAAK):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
        elif(tok.type == Token.LVAR):
            lvar = Node(Token.Token(Token.LVAR, tok.var))
            # checks if the variable has a type
            if(tok.var in vars):
                lvar.left = types[vars.index(tok.var)]
            else:
                print(f"{tok.var} has unkown type")
                print("exit status 1")
                exit(1)
            return True, lvar
        elif(tok.type == Token.LHAAK):
            self.lparentheses += 1
            node = self.expr(Node(Token.Token(Token.EMPTY, "EMPTY")), vars, types)
            tok = self.current_tok
            if(tok.type == Token.RHAAK):
                self.lparentheses -= 1
                return True, node
            else:
                print(f"Syntax error: right bracket not found after an opening left bracket.")
                exit(1)

        return False, Node(Token.Token(Token.EMPTY, "EMPTY"))
    
    # checks if current token is a pexpr or an abstraction
    # returns the corresponding sub abstract syntax tree
    # "leftChild" is used to make applications left-associative
    def lExpr(self, leftChild, vars, types):
        self.advance()
        tok = self.current_tok
        correct, temp = self.pExpr(vars, types)
        # if there is a right paranthesis whithout any left parentheses left
        if(self.lparentheses == 0 and tok.type == Token.RHAAK):
            print(f"Syntax error: right bracket found without an opening left bracket.")
            exit(1)
        elif(correct == True):
            # "leftChild" is used here to make applications left-associative
            if(leftChild.token.type == Token.EMPTY):
                node = temp
            else:
                appl = Node(Token.Token(Token.APPL, "@"))
                appl.left = leftChild
                appl.right = temp
                node = appl
            return True, node
        elif(tok.type == Token.LAMBDA):
            self.advance()
            # making and returning an abstraction
            lamb = Node(Token.Token(Token.LAMBDA, "\\"))
            tok = self.current_tok
            if(tok.type == Token.LVAR):
                lamb.left = Node(Token.Token(Token.LVAR, tok.var))
                temp = tok.var
                self.advance()
                tok = self.current_tok
                if(tok.type != Token.CIRCUMFLEX):
                    print("Syntax error: missing '^'.")
                    print("exit status 1")
                    exit(1)
                
                # getting the type
                correct, circumflex = self.Type()
                # keeping track of the variables and their types
                if(temp in vars):
                    types[vars.index(temp)] = circumflex
                else:
                    vars.append(temp)
                    types.append(circumflex)

                if(correct == False):
                    print("Syntax error: missing type in abstraction.")
                    print("exit status 1")
                    exit(1)
                # variables now also have a child, their type
                lamb.left.left = circumflex
                self.back()
                # checking if it has an expression
                correct, lamb.right = self.lExpr(Node(Token.Token(Token.EMPTY, "EMPTY")), vars, types)
                if(correct == False):
                    print(self.current_tok)
                    print(f"Syntax error: expresssion in abstraction not found.")
                    print("exit status 1")
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
    def exprApo(self, leftChild, vars, types):
        juist, passFurther = self.lExpr(leftChild, vars, types)
        if(juist == True):
            node = self.exprApo(passFurther, vars, types)
            return node
        return leftChild

    # checks if current token is a lexpr if so 
    # returns the corresponding sub abstract syntax tree
    # if not then error is thrown
    # "leftChild" is used to make applications left-associative
    def expr(self, leftChild, vars, types):
        juist, passFurther = self.lExpr(leftChild, vars, types)
        if (juist == False):
            print(f"Syntax error: wrong input.")
            exit(1)
        node = self.exprApo(passFurther, vars, types)
        return node
    
    # checks if current token is ⟨uvar⟩ or '(' ⟨type⟩ ')'
    # returns the corresponding sub abstract syntax tree
    # if not, then error is thrown
    def Type(self):
        self.advance()
        tok = self.current_tok
        if(tok.type == Token.UVAR):
            notEmpty, right = self.TypePrime()
            node = Node(Token.Token(Token.UVAR, tok.var))
            if(notEmpty == True):
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
                
                notEmpty, right = self.TypePrime()
                if(notEmpty == True):
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
            print("Syntax error: wrong ⟨type⟩ input")
            print("exit status 1")
            exit(1)
            
    # checks for '->' ⟨type⟩
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

