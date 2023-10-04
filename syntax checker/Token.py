import string
# from binarytree import Node

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
BSLASH = 'BSLASH'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
EMPTY = 'EMPTY'

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
        if invoer[i] == ' ':
            pass
        elif invoer[i] == '(':
            tokens.append(Token(LHAAK))
        elif invoer[i] == ')':
            tokens.append(Token(RHAAK))
        elif invoer[i] == '\\':
            tokens.append(Token(BSLASH))
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

    return tokens


class biNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        print(self.data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
        
class varNode:
    def __init__(self, var):
        self.var = var
    
    def __repr__(self):
        print(self.var)

def test(lijst):
    lijst[0] += 1
    test2(lijst)
    print(lijst)

def test2(lijst):
    lijst[0] += 1

root = 0
if(root == 0):
    root = biNode(Token(EMPTY))
    if (root.data.soort == EMPTY):
        print('oh lets go')

if (root.data.soort == EMPTY):
    print('oh lets go')


def expr(lijst, ik, cursor):
    print('expr')
    ik[0] = biNode(Token(APPL))
    if(lExpr(lijst, ik[0].left, cursor)):
        if(dashExpr(lijst, ik[0].right, cursor)):
            return True
    else:
        return False

#IKS VERANDEREN
# isempyt, issucces
def dashExpr(lijst, ik, cursor):
    print('dashExpr')
    if(cursor[0] < len(lijst)):
        ik[0] = biNode(Token(APPL))
        if(lExpr(lijst, ik[0].left, cursor) == True):
            teruggegeven = dashExpr(lijst, ik[0].right, cursor)
            if(teruggegeven[1] == True):
                if(teruggegeven[0] == True):
                    ik[0].right = Token(EMPTY)
                    return True, True
                else:
                    dashExpr(lijst, ik[0].right, cursor)
                    return False, True
            else:
                return False, False
        else:
            return True, True


def lExpr(lijst, ik,cursor):
    print('lExpr')
    if(cursor[0] < len(lijst)):
        if(lijst[cursor[0]].soort == BSLASH):
            cursor[0] += 1
            if(lijst[cursor[0]].soort == VAR):
                ik[0] = biNode(Token(BSLASH))
                ik[0].left = varNode(lijst[cursor[0]].var)
                lExpr(lijst, ik[0].right, cursor)
            else:
                return False
        elif (pExpr(lijst, ik[0], cursor) == True):
            return True
        else:
            return False

def pExpr(lijst, ik, cursor):
    print('pExpr')
    if(cursor[0] < len(lijst)):
        if lijst[cursor[0]].soort == LHAAK:
            cursor[0] += 1
            print('LHAAKJE-----------')
            if(expr(lijst, ik[0], cursor) == True):
                if(lijst[cursor[0]].soort == RHAAK):
                    print('RHAAKJE---------------------')
                    cursor[0] += 1
                    return True
                else:
                    return False
            else:
                return False
        elif (lijst[cursor[0]].soort == VAR):
            print('VARIABELE--------------')
            ik[0] = varNode(lijst[cursor[0]].var)
            cursor[0] += 1
            return True
        else:
            return False

def run(invoer):
    verwerkt = verwerk(invoer)

    root = [0]
    cursor = [0]

    expr(verwerkt, root, cursor)
    APPL = 'APPLICATION'

    if (root.data.soort == APPL):
        print('oke lets go')
