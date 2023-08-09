class CreditCard: 
    def __init__(self, cvc, expirationDate, cardNumber): 
        self.cvc = cvc
        self.expirationDate = expirationDate
        self.cardNumber = cardNumber
    
    def getCVC(self):
        return(self.cvc) 
        
    def getExpirationDate(self): 
        return(self.expirationDate)

    def getCardNumber(self): 
        return(self.cardNumber)

class CardProcessor: 
    def __init__(self): 
        pass

    def charge(self, CreditCard, amount):
        #vendor operates charge 
        print(f"Credit Card {CreditCard.cardNumber} has been charged ${amount}")
        pass
        

class ProcessorInfo:
    def __init__(self, orderNumber, isApproved, errorMessage, transDate, transTime): 
        self.orderNumber = orderNumber
        self.isApproved = isApproved
        self.errorMessage = errorMessage
        self.transDate = transDate
        self.transTime = transTime
     
    def getOrderNumber(self): 
        return(self.orderNumber)

    def isApprovedValue(self): 
        return(self.isApproved) 
    
    def getError(self): 
        return(self.errorMessage) 
    
    def getTranDate(self): 
        import datetime
        return(self.transDate)
    
    def getTransTime(self): 
        import datetime
        return(self.transTime)

#Not used in the credit card processing    
class User: 
    def __init__(self, firstName, lastName, email, registered): 
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.registered = registered
    
    def getFirstName(self): 
        return(self.firstName)
    
    def getLastName(self): 
        return(self.lastName)
    
    def getEmail(self): 
        return(self.email)
    
    def KnownUser(self): 
        return(self.registered)


    
#test instance of credit card
user1 = CreditCard(cvc = '323', expirationDate = 'March 8, 2023', cardNumber = '1234 1234 1234 1234') 

print(user1.cvc)
print(user1.expirationDate)
print(user1.cardNumber)

#Take instance of credit card and try to 'charge' the card
cardprocessor = CardProcessor()
#cardprocessor.charge(user1.cvc, user1.expirationDate, user1.cardNumber, total = 123)
cardprocessor.charge(user1,amount = 123)
#cardprocessor.charge(CreditCard.user1, total = 123)   







