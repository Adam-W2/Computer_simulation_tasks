
"""
Test code for the Class "Polynomial"
creates Class "PolynomialTest" to do said test like dog example given


"""

from Polynomial import Polynomial #imports Polynomial class from Polynomial file

class PolynomialTest(object):#copying dog example to create test class
    
    def test(self):
        PolyA = Polynomial([2, 0, 4, -1, 0, 6]) #creating lists to create objects
        PolyB = Polynomial([-1, -3, 0, 4.5, 0, 0])
        
        print("The order is: " + str(PolyA.order()))
        c = Polynomial(PolyA.addition(PolyB)) #assinging c to output of addition
        print("Add poly A to poly B: " + c.getFormatted()) #print statement
        
        d = Polynomial(PolyA.derivative()) #assinging d to output of derivative 
        print("The first derivative of A is: " + d.getFormatted()) #print statement
        
        e = Polynomial(d.antiderivative()) #assinging e to output of derivative 
        print("The antiderivative of A is: "+ e.getFormatted()) #print statement
        
def main(): #main to call test function in the class test (like dog example)
    test1 = PolynomialTest()
    test1.test()
    
main()
 