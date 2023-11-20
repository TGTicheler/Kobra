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
import Checker
# standard library code used for getting and checking the argument file
import os.path
import sys

file = sys.argv[1]

if(os.path.isfile(file)== False):
    print("File not found")
    print("exit status 1")
    exit(1)

lines = open(file).readlines()
for line in lines:
    if (line != '\n'):
        verwerkt = Token.verwerk(line)
        geparset = Parser.Pars(verwerkt)
        root = geparset.parse()
        root.stringPrinten()
        print()
        check = Checker.Checker(root.left, root.right)
        check.check()

print("exit status 0")
exit(0)
