import string

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
BSLASH = 'BSLASH'
VAR = 'VARIABELE'

class Token:
    def __init__(self, soort):
        self.soort = soort

    def __repr__(self):
        return f'{self.soort}'
    

def verwerk(invoer):
    tokens = []
    juist = True
    for i in range(len(invoer)):
        if invoer[i] == '(':
            tokens.append(Token(LHAAK))
        elif invoer[i] == ')':
            tokens.append(Token(RHAAK))
        elif invoer[i] == '\\':
            tokens.append(Token(BSLASH))
        elif invoer[i][0] in string.ascii_lowercase:
            tokens.append(Token(VAR))
        else:
            print("Onjuiste invoer")
            juist = False
            
    print(tokens)
    return tokens, juist

def hallo():
    print('Hello world')
