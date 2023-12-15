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
import reductions
import os.path
import sys

# Checks if the amount of arguments is correct
if len(sys.argv) != 2:
    print("File is needed")
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
        tokens = Token.extractTokens(oneLine) # array of tokens of the given string
        parced = Parser.Pars(tokens)
        root = parced.getRoot() # the root of the ast
        # root.printTree() ---------------------------------------- geen idee of dit ook moet worden uitgeprint
        # print()
        reduceThis = reductions.reduce(root)
        reduced = reduceThis.getReducedTree() # the root of the reduced ast
        reduced.printTree()
        print()

exit(0)