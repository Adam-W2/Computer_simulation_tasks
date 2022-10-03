"""
Nuclei Decay!
Class that when provided values creates an array of nuclei and when prompted decays said nuclei to its simulated halflife
"""
import math
import random

class RadioactiveDecay(object):
   
    def __init__(self, N, lamb, deltat): #initialises all required values to create array object and then decay
        self.N = N
        self.lamb = lamb
        self.deltat = deltat
        
    def createArray(self): #creates array called temp then appends lists called row filled with 1 to create 2D array
        self.temp=[]
        row = [1]*self.N
        for i in range(self.N):
            self.temp.append(row[:])
         
    def decay(self): #decay method used to decay nuclei 
        p = self.lamb * self.deltat #calculated probability of decay
        totaldecay = 0 #create counting systems for total nuclei that decay and how long it takes to reach half the inital nuclei
        timestep = 0.0
        while totaldecay < (math.pow(self.N,2))/2 : #while loop to repeatedly decay until half nuceli are left
            timestep += self.deltat
            for i in range(len(self.temp)): #range for i and j essentially going row then column
                for j in range(len(self.temp)):
                    if self.temp[i][j] == 1: #if statement to check if nuclei has decayed or not
                        r = random.random() #random number generator
                        if r <= p:
                            self.temp[i][j] = 0 #decays nuclei if the random number is less than p
                            totaldecay += 1
                            
                        
                    
        for i in self.temp: #print statements for all required info 
            print(i) 
        print("Initial number of undecayed nuclei: " + str(math.pow(self.N, 2)))
        print("Final number of undecayed nuclei: " + str((math.pow(self.N,2)) - totaldecay))
        print("Simulated half-life: " + str(timestep))
        print("Half-life calculated using decay constant: " + str(math.log(2)/self.lamb))                