"""
Class to test and use the Traffic class
"""
from Traffic import Traffic
import numpy as np
import matplotlib.pyplot as plt

class testTraffic(object): #create class
    
    def test(self): #method to run test function that creates graphical intepretation
        N = int(input("Please input number of cells: "))
        delT = int(input("Please input number of time-steps: "))
        car = float(input("Please input car density: "))
        
        B = Traffic(N, delT, car) #Runs methods from Traffic class 
        B.array()
        B.carMove()
        B.repTraffic()
        
    def simulation(self): #Simulation method to run a simulation using Traffic methods and plot graph
        N = int(input("Please input number of cells: "))
        delT = int(input("Please input number of time-steps: "))
        
        car = np.linspace(0, 1, 100) #create array of car density values
        avspeed = [] #empty list to append to
        
        for i in range(len(car)):
            
            B = Traffic(N, delT, car[i])
            B.array()
            A = B.carMove()
            avspeed.append(A)
            
        
        plt.plot(car, avspeed) #plots graph
        plt.xlabel("Car density")
        plt.ylabel("Average stable state speed")
        plt.show
        
def main(): #main function to run anything
    run = testTraffic()
    Y = int(input("Which method would you like to run, 1 for test, 2 for simulation: "))
    if Y == 1:
        run.test()
    else:
        run.simulation()
    
main()