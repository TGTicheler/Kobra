#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 
# Paul Tielens s3612031 ...
# Concepts of Programming Languages, 2023


import Token
import Parser
import reductions

# leest vanuit de command line in
print("Filename: ")
file = input('---< ')
invoer = "\n"
with open(file) as f:
    while (invoer == "\n"): #pakt de eerste regel die tekst erin heeft staan
        invoer = f.readline()
verwerkt = Token.verwerk(invoer)
geparset = Parser.Pars(verwerkt)
root = geparset.parse()
reduceThis = reductions.reduce(root)
reduced = reduceThis.run()


print("exit status 1")
exit(0)
