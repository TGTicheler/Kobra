import Parser
import Token

class check:
    def __init__(self, expression, type):
        self.expression = expression
        self.type = type
        self.madeType = None
        


    # def giveCorrectType(self, node):


    def typeCheck(self, node, vars, types):


