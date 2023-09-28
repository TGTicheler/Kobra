#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 


import Token

# leest vanuit de command line in
invoer = input('---< ')

geknipt = invoer.split(' ')
#filtert de lege elementen uit geknipt
gefilterd = list(filter(None, geknipt))

print(geknipt)
print(gefilterd)

verwerkt = Token.verwerk(gefilterd)
print(f'verwerkt: {verwerkt}')
