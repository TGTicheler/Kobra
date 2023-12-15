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

# goes through the file given as a command line argument
# gets multiple judgements and checks if they are correct

import Token
import Parser
import Checker
# standard library code used for getting and checking the argument file
import os.path
import sys

# Checks if the amount of arguments is correct
if len(sys.argv) != 2:
    print("One command line argument is needed")
    exit(1)

# Checks if the given file can be opened
file = sys.argv[1]
if(os.path.isfile(file)== False):
    print("File not found")
    exit(1)

# reads all the lines of the given file
lines = open(file).readlines()
for oneLine in lines:
    if (oneLine != '\n'):
        tokens = Token.verwerk(oneLine) # array of tokens of the given string
        parced = Parser.Pars(tokens)
        root = parced.getRoot() # the root of the ast

        Checker.Checker(root.left, root.right) # checks if the judgement is correct
        root.printTree()
        print()

exit(0)