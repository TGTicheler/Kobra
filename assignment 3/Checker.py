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

import Parser
import Token

class Checker:
    def __init__(self, expression, type):
        self.expression = expression
        self.type = type
        self.madeType = self.typeCheck(self.expression)
        str1 = ""
        str2 = ""
        str1 = self.madeType.giveTreeInString(str1)
        str2 = self.type.giveTreeInString(str2)
        if(str1 != str2):
            print("error: Expression and Type do not match")
            print("exit status 1")
            exit(1)


    def typeCheck(self, node):
        if(node.token.type == Token.LAMBDA):
            to = Parser.Node(Token.Token(Token.TO, "->"))
            to.left = self.typeCheck(node.left)
            to.right = self.typeCheck(node.right)
            return to
        elif(node.token.type == Token.APPL):
            left = self.typeCheck(node.left)
            right = self.typeCheck(node.right)
            strLeftLeft = ""
            strRight = ""
            strLeftLeft = left.left.giveTreeInString(strLeftLeft)
            strRight = right.giveTreeInString(strRight)

            if(left.token.type == Token.TO and strLeftLeft == strRight ):
                return left.right
            else:
                print("deze error")
                print("exit status 1")
                exit(1)
        elif(node.token.type == Token.LVAR):
            return node.left
        else:
            print("error")
            print("exit status 1")
            exit(1)



