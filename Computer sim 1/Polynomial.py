
"""
Creation of Class "Polynomial" which can add, do derivation integral and then format the outputted polynomial

"""
class Polynomial(object): #defines class Polynomial as object
    coefficients = []
    size = 0
    def __init__(self, coefficients): #initalises polynomial varible to be used in code
        self.coefficients = coefficients
        self.size = len(coefficients)
        
    def order(self): #to get the order of polynomial we take the length of the list
        return self.size - 1

    def addition(self, polyB): #adding together two polynomials
        c  = self.size if self.size >= len(polyB.getValue()) else len(polyB.getValue) #checks the length of coefficient list and changes the length of the temporary list if polyB is bigger
            
        temp = [0] * c #sets length of temp with c
        
        for i in range(len(self.coefficients)): #for loop used to go through each i to add together the two coefficients
            temp[i] = self.coefficients[i] + polyB.getValue()[i]
        return temp
    
    def getValue(self): #used to encapsulate the polyB list for addition()
        return self.coefficients
    
    def derivative(self): #input polynomial outputs derivative of that polynomial
        temp = [] #create empty list 
        
        for i in range(len(self.coefficients) - 1): #for loop to go through each coefficient and output the derivaitve 
            
            temp.append(self.coefficients[i + 1] * (i+1))
            
        return temp
    
    def antiderivative(self): #input polynomial outputs integral of that polynomial
        temp = []
        
        for i in range(len(self.coefficients) + 1): #for loop that iterates through each value and outputs the integral and appends to empty list
            if i == 0:
                temp.append(2) #adds constant of integration
            else:
                temp.append(self.coefficients[i - 1] * 1/(i))

        return temp 
    
    def getFormatted(self):
        s = "(" #creates string so we can add coefficients to string
        power = 0 #power so we can keep track of what power the polynomial is
        
        for i in range(len(self.coefficients)): #for loop to check each coefficient and add to the string accordingly
            if self.coefficients[i] > 0.0:
                if i == 0: #essentially stops there being a plus or minus at the start
                    s += ""
                elif i == 1 and self.coefficients[0] == 0:
                    s += ""
                else:
                    s += " + "
                                    
                if power > 1: #power used to add number at the end of each coefficient  
                    s += str(self.coefficients[i]) + "x^" + str(power)
                    
                elif power == 1:
                    s += str(self.coefficients[i]) + "x"
                    
                else:
                    s += str(self.coefficients[i])
                    
            elif self.coefficients[i] == 0:
                s+= ""
                
            elif self.coefficients[i] < 0.0: #does same as positive but adds negative sign instead
                if i < len(self.coefficients):
                    s += "- " if i == 0 else " - "
                    
                if power > 1:
                    s += str(self.coefficients[i] * -1) + "x^" + str(power)
                    
                elif power == 1:
                    s += str(self.coefficients[i] * -1) + "x"
                
                else:
                    s += str(self.coefficients[i] * -1)
            power += 1 #adds one to the power each loop so we get increasing power every loop
        s +=")" #adds end bracket :D
        return s
                
                
    
    
    
    
    
    
    
    
