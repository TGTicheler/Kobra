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

# checks if the expression in the judgement matches its type

import Parser
import Token

# takes in 2 ast's an expression and its type and checks if they match
class Checker:
    def __init__(self, expression, givenType):
        self.expression = expression
        self.givenType = givenType
        self.derivedType = self.deriveType(self.expression) # the type is derived from the expression
        # comparing the ast's directly didn't work
        # so they are translated into a string and the strings are then compared
        str1 = ""
        str2 = ""
        str1 = self.derivedType.giveTypeInString(str1)
        str2 = self.givenType.giveTypeInString(str2)
        if(str1 != str2):
            print("error: Expression and Type do not match")
            print("exit status 1")
            exit(1)


    # the following is used in the function below:
    # S can be any type for example ((A -> B) -> C)
    # (\x ^ A (S)) is translated to (A -> S)
    # ((S1 -> S2) S1) is translated to S2
    # x has a type S, so this is translated to S

    # the type is derived from an expression
    def deriveType(self, node):
        if(node.token.type == Token.LAMBDA):
            to = Parser.Node(Token.Token(Token.TO, "->"))
            to.left = self.deriveType(node.left)
            to.right = self.deriveType(node.right)
            return to
        elif(node.token.type == Token.APPL):
            left = self.deriveType(node.left)
            right = self.deriveType(node.right)
            # comparing the ast's directly didn't work
            # so they are translated into a string and the strings are then compared
            strLeftLeft = ""
            strRight = ""
            strLeftLeft = left.left.giveTypeInString(strLeftLeft)
            strRight = right.giveTypeInString(strRight)

            if(left.token.type == Token.TO and strLeftLeft == strRight ):
                return left.right
            else:
                print("Types are not matching")
                print("exit status 1")
                exit(1)
        elif(node.token.type == Token.LVAR):
            return node.left
        else:
            print("Type is wrong")
            print("exit status 1")
            exit(1)



