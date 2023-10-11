#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

import Token
import Parser
import string

# leest vanuit de command line in
invoer = input('---< ')

verwerkt = Token.verwerk(invoer)
print(verwerkt)
geparset = Parser.Pars(verwerkt)
ast = geparset.parse()
print(ast)


exit(1)
