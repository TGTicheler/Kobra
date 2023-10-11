import Token

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'

class biNode:
    def __init__(self, data, var):
        self.left = None
        self.right = None
        self.data = data
        self.var = var
        self.parent = None

    def __repr__(self):
        self.PrintTree()

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        print(self.var)

        if self.right:
            self.right.PrintTree()
                
class varNode:
    def __init__(self, var):
        self.var = var
        self.parent = None
    
    def __repr__(self):
        print(self.var)

    def PrintTree(self):
        print(self.var)


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
        self.expr(self.root)
        self.root.printTree()
        return self.root
    
    def pExpr(self):
        print('in pExpr')
        tok = self.current_tok
        print(f' \t \t tok:  {tok}')
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit(0)
        elif(tok.soort == VAR):
            print(f'Variabele: {tok}')
            return True, varNode(tok.var)
        elif(tok.soort == LHAAK):
            print('Lhaakje')
            self.lhaakjes += 1
            juist, node = self.expr()
            if(juist == True):
                tok = self.current_tok
                if(tok.soort == RHAAK):
                    self.lhaakjes -= 1
                    print('Rhaakje')
                    return True, node
                else:
                    print('ERROR geen Rhaakje --------------')
                    exit(0)
            else:
                print('ERROR geen expressie in ( )---------------')
                exit(0)
        else:
            return False
        
    def lExpr(self):
        print('in lExpr')
        self.advance()
        tok = self.current_tok
        print(f' \t \t tok:  {tok}')
        juist, node = self.pExpr()
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit(0)
        elif(juist == True):
            return True, node
        elif(tok.soort == LAMBDA):
            print('Lambda')
            self.advance()
            node = biNode(Token(LAMBDA), "\\")
            tok = self.current_tok
            if(tok.soort == VAR):
                node.left 
                print(f'Variabele {tok}')
                if(self.lExpr() == False):
                    print('ERROR mist lExpr-------------')
                    exit(0)
            else:
                print('ERROR geen variabele bij Lambda-----------------')
                exit(0)
        else:
            return False
    
    def dashExpr(self):
        print('in dashExpr')
        if(self.lExpr() == True):
            print('in dashExpr lExpr is True so dashExpr')
            self.dashExpr()




    def expr(self):
        print('in expr')
        if (self.lExpr() == False):
            return False
        self.dashExpr()
        return True