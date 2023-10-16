# Paul Tielens s3612031 ...
# Concepts of Programming Languages, 2023

# Parses an array of tokens of lambda calculus and makes a binary tree

import Token

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

class Node:
    def __init__(self, token):
        self.left = None
        self.right = None
        self.token = token
        self.parent = None

    def __repr__(self):
        if self.type == VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'

    #pre-order
    def PrintTree(self):
        print(self.token.var, " ", end= "")

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()



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
        self.stringTeruggeven(self.root)
        print()
        return self.root

    
    def stringTeruggeven(self, node):
        if(node.token.soort == VAR):
            print(node.token.var, end="")
            return

        print("(", end="")

        if (node.token.soort == LAMBDA):
            print(f"{node.token.var}", end="")
            self.stringTeruggeven(node.left)
            print(" ", end="")
            self.stringTeruggeven(node.right)
        elif (node.token.soort == APPL):
            self.stringTeruggeven(node.left)
            print(" ", end="")
            self.stringTeruggeven(node.right)

        print(")", end="")


        


    def pExpr(self):
        tok = self.current_tok
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit(0)
        elif(tok.soort == VAR):
            return True, Node(Token.Token(VAR, tok.var))
        elif(tok.soort == LHAAK):
            self.lhaakjes += 1
            juist, node = self.expr()
            if(juist == True):
                tok = self.current_tok
                if(tok.soort == RHAAK):
                    self.lhaakjes -= 1
                    return True, node
                else:
                    print('ERROR geen Rhaakje --------------')
                    exit(0)
            else:
                print('ERROR geen expressie in ( )---------------')
                exit(0)

        return False, Node(Token.Token(EMPTY, "EMPTY"))
        
    def lExpr(self):
        self.advance()
        tok = self.current_tok
        juist, node = self.pExpr()
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            exit(0)
        elif(juist == True):
            return True, node
        elif(tok.soort == LAMBDA):
            self.advance()
            node = Node(Token.Token(LAMBDA, "\\"))
            tok = self.current_tok
            if(tok.soort == VAR):
                node.left = Node(Token.Token(VAR, tok.var))
                juist, node.right = self.lExpr()
                if(juist == False):
                    print('ERROR mist lExpr-------------')
                    exit(0)
                return True, node
            else:
                print('ERROR geen variabele bij Lambda-----------------')
                exit(0)
        
        return False, Node(Token.Token(EMPTY, "EMPTY"))
    
    def dashExpr(self):
        juist, left = self.lExpr()
        if(juist == True):
            nietLeeg, right = self.dashExpr()
            if(nietLeeg == True):
                node = Node(Token.Token(APPL, "@"))
                node.left = left
                node.right = right
            else:
                node = left
            return True, node
        return False, Node(Token.Token(EMPTY, "EMPTY"))

    def expr(self):
        juist, left = self.lExpr()
        if (juist == False):
            print("Onjuiste invoer")
            exit(0)
        nietLeeg, right = self.dashExpr()
        if(nietLeeg == True):
            node = Node(Token.Token(APPL, "@"))
            node.left = left
            node.right = right
        else:
            node = left
        return True, node
    
def connectFamily(node):
    if node.left != None:
        node.left.parent = node
        node.left = connectFamily(node.left)

    if node.right != None:
        node.right.parient = node
        node.right = connectFamily(node.right)

    return node
