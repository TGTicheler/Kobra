import string
import Token
import Parser

invoer = "A -> B -> C -> D"


verwerkt = Token.verwerk(invoer)
geparset = Parser.Pars(verwerkt)
boeie, root = geparset.Type()
root.stringTeruggeven()
print()