import string
import reductions

test = ["a", "b"]
opties = ["a", "b", "c"]

def makeVar(opties,vars):
    for i in range(len(opties)):
        if(opties[i] not in vars):
            return opties[i]
    


new =makeVar(opties, opties)
print(new)