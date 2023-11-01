import Parser
import Token

class Checker:
    def __init__(self, expression, type):
        self.expression = expression
        self.type = type
        self.madeType = None

    def check(self):
        self.madeType = self.typeCheck(self.expression)
        if(self.madeType == self.type):
            print("lets go")
        else:
            print("noooo")



    def typeCheck(self, node):
        print(node.token)
        if(node.token.type == Token.LAMBDA):
            to = Parser.Node(Token.Token(Token.TO, "->"))
            to.left = self.typeCheck(node.left)
            to.right = self.typeCheck(node.right)
            return to
        elif(node.token.type == Token.APPL):
            left = self.typeCheck(node.left)
            right = self.typeCheck(node.right)
            if(left.token.type == Token.TO and left.left == right):
                return left.right
            else:
                print("deze error")
                print("exit status 1")
                exit(1)
        elif(node.token.type == Token.LVAR):
            print(node.left.token)
            return node.left
            
        else:
            print("error")
            print("exit status 1")
            exit(1)



