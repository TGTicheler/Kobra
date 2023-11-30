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
    print("One command line argument is needed")
    print("exit status 1")
    exit(1)

# Checks if the given file can be opened
file = sys.argv[1]
if(os.path.isfile(file)== False):
    print("File not found")
    print("exit status 1")
    exit(1)

# reads only the first line from the given file
with open(file) as f:
    firstLine = f.readline()

tokens = Token.extractTokens(firstLine) # array of tokens of the string
obj = Parser.Pars(tokens)
root = obj.getRoot() # the root of the ast of the unreduced expression
root.printTree()
print()
reduceThis = reductions.reduce(root)
reduced = reduceThis.getReducedTree()
reduced.printTree()
print()

print("exit status 0")
exit(0)
