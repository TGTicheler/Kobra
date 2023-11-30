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

# takes in a string and produces an array of tokens from the string

import string

LPAR = 'LEFT PARENTHESIS'
RPAR = 'RIGHT PARENTHESIS'
LAMBDA = 'LAMBDA'
VAR = 'VARIABELE'
APPL = 'APPLICATION'
END = 'END'
EMPTY = 'EMPTY'

# token objects 
class Token:
    def __init__(self, type, var):
        self.type = type
        self.var = var

    def __repr__(self):
        if self.type == VAR:
            return f'{self.type}:{self.var}'
        return f'{self.type}'
    
# gets a string gives the tokens of the string
# and checks if there are illegal characters
def extractTokens(givenString):
    tokens = []
    size = len(givenString)
    i = 0
    # goes through the string and creates an array of tokens
    while i < size:
        if givenString[i] == ' ' or givenString[i] == '\n' or givenString[i] == '\r':
            pass # these are skipped
        elif givenString[i] == '(':
            tokens.append(Token(LPAR, "("))
        elif givenString[i] == ')':
            tokens.append(Token(RPAR, ")"))
        elif givenString[i] == '\\' or givenString[i] == 'λ':
            tokens.append(Token(LAMBDA, "\\"))
        elif givenString[i] in string.ascii_letters:
            var = ''
            # one variable can have multiple letters or digits
            while(givenString[i] in string.ascii_letters or givenString[i].isnumeric()):
                var = var + givenString[i]
                i += 1
                if(i >= size):
                    break
            i -= 1
            tokens.append(Token(VAR, var))
        else:
            print(f"Syntax error: wrong input.")
            exit(1)
        i += 1

    tokens.append(Token(END, "END")) # End of tokens

    return tokens