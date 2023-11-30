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

# Takes in a string of Lambda calculus, which is then parsed

import Token
import Parser
import sys
import os.path

# can read a whole file or a string from stdin, depending on the number of command line arguments
if(len(sys.argv) == 1):
    toBeParced = {input()} # only 1 string needs to be parced
elif(len(sys.argv) == 2):
    file = sys.argv[1]

    #checks if the file exists
    if(os.path.isfile(file)== False):
        print("File not found")
        print("exit status 1")
        exit(1)

    toBeParced = open(file).readlines() # all the strings in the file
else:
    print("Only 0 or 1 command line arguments can be given")
    print("exit status 1")
    exit(1)

# all the strings in "lines" are being parced
for currentString in toBeParced:
    if (currentString != '\n'):
        tokens = Token.extractTokens(currentString) # array of tokens of the given string
        parced = Parser.Pars(tokens)
        root = parced.getRoot() # the root of the ast
        root.printTree()
        print()

print("exit status 0")
exit(0)