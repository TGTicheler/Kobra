#Beetje testen

#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

# leest vanuit de command line in
invoer = input('---< ')

geknipt = invoer.split(' ')
#filtert de lege elementen uit geknipt
gefiltert = list(filter(None, geknipt))

print(geknipt)
print(gefiltert)