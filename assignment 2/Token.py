# Paul Tielens s3612031
# Thom Ticheler s3696820
# Laura Faas s3443159
# Concepts of Programming Languages, 2023

# takes in a string and produces an array of tokens from the string

import string

LHAAK = 'L-HAAKJE'
RHAAK = 'R-HAAKJE'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

class Token:
    def __init__(self, type, var):
        self.type = type
        self.var = var

    def __repr__(self):
        if self.type == VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'
    

def verwerk(invoer):
    tokens = []
    grootte = len(invoer)
    i = 0
    while i < grootte:
        if invoer[i] == ' ' or invoer[i] == '\n' or invoer[i] == '\r':
            pass
        elif invoer[i] == '(':
            tokens.append(Token(LHAAK, "("))
        elif invoer[i] == ')':
            tokens.append(Token(RHAAK, ")"))
        elif invoer[i] == '\\' or invoer[i] == 'λ':
            tokens.append(Token(LAMBDA, "\\"))
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
            exit(0)
        i += 1

    tokens.append(Token(END, "END"))

    return tokens
