
"""
Mandelbrot set
two things
1. how to update the required variable
2. how to set-up the while loop

"""
import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot(object):
    
    def __init__(self, xrange, yrange, N): #initilise function in order to use them in the class
        self.xrange = xrange
        self.yrange = yrange
        self.N = N
    
    def array(self): #creates three 2D numpy arrays an XX coordinate, YY coordinate and the complex numbers used Z
        X = np.linspace(self.xrange[0], self.xrange[1], self.N) #using numpy linspace to create these 1D arrays
        Y = np.linspace(self.yrange[0], self.yrange[1], self.N) 
        
        self.XX, self.YY = np.meshgrid(X, Y) #using mesh grid to then create two 2D arrays
        self.Z = self.XX + 1j * self.YY #creates complex numbers
        
    def mandelbrot(self, C): #creates a function that checks if the complex number is in the mandelbrot set
            z = 0
            p = 0
            
            while abs(z) < 2 and p < 255: #two conditions for a while loop, keeps adding to p 
                z = z * z + C #formula
                p += 1
        
            return p
    
    def plot(self): #plotting method
        
        mandelbrot_vec = np.vectorize(self.mandelbrot) #In order to use the mandelbrot method with the vector array we have to vectorise it
        N = mandelbrot_vec(self.Z) #then input the complex array into the newly vectorised function
        plt.pcolormesh(self.XX, self.YY, N, shading = "auto") #plot using pcolormesh
        
        plt.show()
        