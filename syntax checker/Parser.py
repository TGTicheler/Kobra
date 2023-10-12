import Token

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'

class biNode:
    def __init__(self, var):
        self.left = None
        self.right = None
        self.var = var
        self.parent = None

    def __repr__(self):
        self.PrintTree()
        print()

    #pre-order
    def PrintTree(self):
        print(self.var, " ", end= "")

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()
                
class varNode:
    def __init__(self, var):
        self.var = var
        self.parent = None
    
    def __repr__(self):
        print(self.var)

    def PrintTree(self):
        print(self.var, " ", end= "")


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
        return self.root
    
    def pExpr(self):
        tok = self.current_tok
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit(0)
        elif(tok.soort == VAR):
            return True, varNode(tok.var)
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

        return False, varNode("EMPTY")
        
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
            node = biNode("\\")
            tok = self.current_tok
            if(tok.soort == VAR):
                node.left = varNode(tok.var)
                juist, node.right = self.lExpr()
                if(juist == False):
                    print('ERROR mist lExpr-------------')
                    exit(0)
                return True, node
            else:
                print('ERROR geen variabele bij Lambda-----------------')
                exit(0)
        
        return False, varNode("EMPTY")
    
    def dashExpr(self):
        juist, left = self.lExpr()
        if(juist == True):
            nietLeeg, right = self.dashExpr()
            if(nietLeeg == True):
                node = biNode( "@")
                node.left = left
                node.right = right
            else:
                node = left
            return True, node
        return False, varNode("EMPTY")

    def expr(self):
        juist, left = self.lExpr()
        if (juist == False):
            print("Onjuiste invoer")
            exit(0)
        nietLeeg, right = self.dashExpr()
        if(nietLeeg == True):
            node = biNode( "@")
            node.left = left
            node.right = right
        else:
            node = left
        return True, node