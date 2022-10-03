
"""
timestep is 100 
so 300 N
"""
#import stuff
from Planet1 import Planet
from Simulation import Simulation
import numpy as np

#define test simulation class
class testSimulation(object):
    
    #creates method to run everything
    def test(self):
        
        #file reading method, not general
        filein = open("Mars.txt", "r")
        
        temp1 = filein.read().splitlines()
        print(temp1)
        filein.close
        
        tokens1 = temp1[2].split(",")
        a = np.array((int(tokens1[0]), int(tokens1[1])))

        tokens2 = temp1[3].split(",")
        b = np.array((int(tokens2[0]), int(tokens2[1])))

        tokens3 = temp1[4].split(",")
        c = np.array((int(tokens3[0]), int(tokens3[1])))
        
        mars = Planet(temp1[0], float(temp1[1]), a, b, c)
        
        filein = open("Phobos.txt", "r")
        
        temp2 = filein.read().splitlines()
        filein.close
        
        tokens1 = temp1[2].split(",")
        a = np.array((int(tokens1[0]), int(tokens1[1])))

        tokens2 = temp1[3].split(",")
        b = np.array((int(tokens2[0]), int(tokens2[1])))

        tokens3 = temp1[4].split(",")
        c = np.array((int(tokens3[0]), int(tokens3[1])))
        
        filein.close
        phobos = Planet(temp2[0], float(temp2[1]), a, b, c)
        
        A = Simulation(70, 500, mars, phobos)
        A.initialCons()
        A.run(mars, phobos)
        
        
            
#main function to run whole simulation    
def main():
    run = testSimulation()
    run.test()
    
main()