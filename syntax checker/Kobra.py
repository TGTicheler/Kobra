#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

import Token
import Parser

# leest vanuit de command line in
invoer = input('---< ')

verwerkt = Token.verwerk(invoer)
geparset = Parser.Pars(verwerkt)
root = geparset.parse()

exit(1)
