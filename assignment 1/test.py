import Token
import Parser

def test(node):
    if(node.token.type == Token.EMPTY):
        print("het herkent het")
    else:
        print("het herkent het niet")

root = Parser.Node(Token.Token(Token.EMPTY, "EMPTY"))

test(Parser.Node(Token.Token(Token.EMPTY, "EMPTY")))