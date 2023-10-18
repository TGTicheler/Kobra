#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 
# Paul Tielens s3612031 ...
# Concepts of Programming Languages, 2023


import Token as Token
import Parser

# leest vanuit de command line in
print("Filename: ")
invoer = input('---< ')
verwerkt = Token.verwerk(invoer)
geparset = Parser.Pars(verwerkt)
root = geparset.parse()

exit(1)
