import string
# from binarytree import Node

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'

class Token:
    def __init__(self, soort, var=None):
        self.soort = soort
        self.var = var

    def __repr__(self):
        if self.var:
            return f'{self.soort}:{self.var}'
        return f'{self.soort}'
    

def verwerk(invoer):
    tokens = []
    grootte = len(invoer)
    i = 0
    while i < grootte:
        if invoer[i] == ' ' or invoer[i] == '\n' or invoer[i] == '\r':
            pass
        elif invoer[i] == '(':
            tokens.append(Token(LHAAK))
        elif invoer[i] == ')':
            tokens.append(Token(RHAAK))
        elif invoer[i] == '\\':
            tokens.append(Token(LAMBDA))
        elif invoer[i] in string.ascii_letters:
            var = ''
            while(invoer[i] in string.ascii_letters or invoer[i].isnumeric()):
                var = var + invoer[i]
                i += 1
                if(i >= grootte):
                    break
            i-=1
            tokens.append(Token(VAR, var))
        else:
            print(f"Onjuiste invoer")
            exit()
        i += 1

    tokens.append(Token(END))

    return tokens


class biNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        print(self.data)

    def PrintTree(self):
        print('yo yo')
        if self.left == varNode('a'):
            print('waarom werkt dit')

        if self.left:
            self.left.PrintTree()
            print('oh toch wel')
        print(self.data),
        if self.right:
            self.right.PrintTree()
            print('andere toch wel')
        
class varNode:
    def __init__(self, var):
        self.var = var
    
    def __repr__(self):
        print(self.var)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.lhaakjes = 0


    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        return res
    
    def pExpr(self):
        print('in pExpr')
        tok = self.current_tok
        print(f' \t \t tok:  {tok}')
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit()
        elif(tok.soort == VAR):
            print(f'Variabele: {tok}')
            return True
        elif(tok.soort == LHAAK):
            print('Lhaakje')
            self.lhaakjes += 1
            if(self.expr() == True):
                tok = self.current_tok
                if(tok.soort == RHAAK):
                    self.lhaakjes -= 1
                    print('Rhaakje')
                    return True
                else:
                    print('ERROR geen Rhaakje --------------')
                    exit()
            else:
                print('ERROR geen expressie in ( )---------------')
                exit()
        else:
            return False
        
    def lExpr(self):
        print('in lExpr')
        self.advance()
        tok = self.current_tok
        print(f' \t \t tok:  {tok}')
        if(self.lhaakjes == 0 and tok.soort == RHAAK):
            print('ERROR een rhaakje zonder lhaakje---------')
            exit()
        elif(tok.soort == LAMBDA):
            print('Lambda')
            self.advance()
            tok = self.current_tok
            if(tok.soort == VAR):
                print(f'Variabele {tok}')
                if(self.lExpr() == False):
                    print('ERROR mist lExpr-------------')
                    exit()
            else:
                print('ERROR geen variabele bij Lambda-----------------')
                exit()
        elif(self.pExpr() == True):
            return True
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


# def expr(lijst, ik, cursor):
#     print('expr')
#     if(cursor[0] < len(lijst)):
#         ik = biNode(Token(APPL))
#         if(lExpr(lijst, ik.left, cursor)):
#             gegeven = dashExpr(lijst, ik.right, cursor)
#             if(gegeven[1] == True):
#                 return True
#             else:
#                 return False
#         else:
#             return False

# #IKS VERANDEREN
# # isempyt, issucces
# def dashExpr(lijst, ik, cursor):
#     print('dashExpr')
#     if(cursor[0] < len(lijst)):
#         ik = biNode(Token(APPL))
#         if(lExpr(lijst, ik.left, cursor) == True):
#             teruggegeven = dashExpr(lijst, ik.right, cursor)
#             if(teruggegeven[1] == True):
#                 if(teruggegeven[0] == True):
#                     ik.right = Token(EMPTY)
#                     return True, True
#                 else:
#                     dashExpr(lijst, ik.right, cursor)
#                     return False, True
#             else:
#                 return False, False
#         else:
#             return True, True


# def lExpr(lijst, ik, cursor):
#     print('lExpr')
#     if(cursor[0] < len(lijst)):
#         if(lijst[cursor[0]].soort == LAMBDA):
#             cursor[0] += 1
#             if(lijst[cursor[0]].soort == VAR):
#                 ik = biNode(Token(LAMBDA))
#                 ik.left = varNode(lijst[cursor[0]].var)
#                 lExpr(lijst, ik.right, cursor)
#             else:
#                 return False
#         elif (pExpr(lijst, ik, cursor) == True):
#             return True
#         else:
#             return False

# def pExpr(lijst, ik, cursor):
#     print('pExpr')
#     if(cursor[0] < len(lijst)):
#         if lijst[cursor[0]].soort == LHAAK:
#             cursor[0] += 1
#             print('LHAAKJE-----------')
#             if(expr(lijst, ik, cursor) == True):
#                 if(lijst[cursor[0]].soort == RHAAK):
#                     print('RHAAKJE---------------------')
#                     cursor[0] += 1
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         elif (lijst[cursor[0]].soort == VAR):
#             print('VARIABELE--------------')
#             ik = varNode(lijst[cursor[0]].var)
#             cursor[0] += 1
#             return True
#         else:
#             return False

def run(invoer):
    verwerkt = verwerk(invoer)
    print(verwerkt)
    parser = Parser(verwerkt)
    ast = parser.parse()

    
