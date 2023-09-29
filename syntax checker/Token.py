import string

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
BSLASH = 'BSLASH'
VAR = 'VARIABELE'

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
            while(invoer[i].isalpha() or invoer[i].isnumeric()):
                var = var + invoer[i]
                print(i)
                i += 1
            i-=1
            tokens.append(Token(VAR, var))
        else:
            print(f"Onjuiste invoer")
            exit()
        i += 1

    return tokens

# def check(tokens):
#     geefDoor = []
#     if()
