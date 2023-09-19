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

import Token
import Parser

givenString = input() 
tokens = Token.verwerk(givenString) # array of tokens of the given string
obj = Parser.Pars(tokens)
root = obj.getRoot() # the root of the ast
root.printTree()
print()

print("exit status 0")
exit(0)