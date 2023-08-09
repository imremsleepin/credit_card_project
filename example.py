# BASE CASE TESTING ENVIRONMENT 


# TEST 1 
# Initial Question: What is the result of return(self)?
# Hypothesis: 
# Solution: Syntax mistake on my end, self. 

class Example: 
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName

    def letsGo(self): 
        print("This works")
        return(self.firstName)

rmayers = Example("Raul","Mayers")
rmayers.letsGo()