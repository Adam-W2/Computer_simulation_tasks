"""
Traffic simulation

"""
import numpy as np
import random
import matplotlib.pyplot as plt #imports things 

class Traffic(object): #creates class 
    
    def __init__(self, N, delT, car): #constructor
        self.N = N
        self.delT = delT
        self.car = car
    
    def array(self): #creates arrays of 0 then populates with 1 depending on car density
        self.cartotal = 0
        self.A = np.zeros((self.delT, self.N)) #numpy array ofc cause its easier
        for j in range(self.N):
            r = random.random() #random number to compare car 
            if r <= self.car: #if random number is less than the car density a "car" is generated
                self.A[0,j] = 1
                self.cartotal += 1
        
    def carMove(self): #method to move all cars
        for i in range(self.delT - 1): #Each if else statement checks certain conditions whether to move the car or not
            move = 0
            for j in range(self.N): #Essentially the rules of the simulation; see notes for more details
                
                if j + 1 == self.N:
                    j = -1
                    
                if self.A[i, j] == 1:
                    if self.A[i, j + 1] == 1:
                        self.A[i + 1,j] = 1
                    else:
                        move += 1
                        self.A[i + 1,j] = 0
                
                else:
                    if self.A[i, j - 1] == 1:
                        self.A[i + 1, j] = 1
                    else:
                        self.A[i + 1, j] = 0
            if self.cartotal == 0: #statement to stop divide by 0 errors
                avspeed = 0
            else:
                avspeed = move/self.cartotal
                
            print("The average speed is: " + str(avspeed)) #print statement
        print(self.A) #shows matrix graphi
        return avspeed
        
    def repTraffic(self): #plots visual representation of the matrix
        
        plt.imshow(self.A[:,:],interpolation = "none", origin = "lower")
        plt.show() #thank you for coming to my ted talk
        
                        
                        
