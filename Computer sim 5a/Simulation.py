"""
Class simulation for a simulation of mars and phobos two body system
"""
#importing stuff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#define class
class Simulation(object):
    #initialise all needed values
    def __init__(self,timestep, N, mars, phobos):
        self.timestep = timestep
        self.N = N
        self.mars = mars
        self.phobos = phobos
        #a clock to print kinetic energy at intervals
        self.step = 0
        
    #sets initial conditions
    def initialCons(self):
        
        self.mars.set_coords(np.array((0, 0)))  # mars
        self.mars.set_velocity(np.array((0, 0)))
        self.mars.set_acceleration(np.array((0, 0)))
        
        self.phobos.set_coords(np.array((9.3773e6, 0)))  # orbital radius of phobos
        
        v_mag = (6.67e-11 * self.mars.get_mass() / np.linalg.norm(self.phobos.get_coords() - self.mars.get_coords()))**(1/2)
        
        self.phobos.set_velocity(np.array((0, v_mag)))
        self.phobos.set_acceleration(np.array((0, 0)))
        
    #update method for each body, is not general
    def update(self):
        G = 6.67e-11
        
        d1 = self.mars.get_coords() - self.phobos.get_coords()
        
            # acceleration of mars
        self.mars.set_acceleration(-(G * self.phobos.get_mass()) / (np.linalg.norm(d1)**2) * d1/np.linalg.norm(d1))

        # phobos pos - mars pos
        d2 = self.phobos.get_coords() - self.mars.get_coords()
       
        # acceleration of phobos
        self.phobos.set_acceleration(-(G * self.mars.get_mass()) / (np.linalg.norm(d2)**2) * d2/np.linalg.norm(d2))

        # v = v + a * timestep
        self.mars.set_velocity(self.mars.get_velocity() + self.mars.get_acceleration() * self.timestep)

        self.phobos.set_velocity(self.phobos.get_velocity() + self.phobos.get_acceleration() * self.timestep)

        # coord system
        self.mars.set_coords(self.mars.get_coords() + (self.mars.get_velocity() * self.timestep))
        self.phobos.set_coords(self.phobos.get_coords() + (self.phobos.get_velocity() * self.timestep))
        
        #condition for calculating and printing out the kinetic energy
        if self.step % 1000 == 0:
            
            mars_kinetic = 1/2 * self.mars.get_mass() * (self.mars.get_velocity())**2
            phobos_kinetic = 1/2 * self.phobos.get_mass() * (self.phobos.get_velocity())**2
        
            T = mars_kinetic + phobos_kinetic
            mag_T = np.linalg.norm(T)
            print(mag_T)
        #adds timestep to step for clock
        self.step += self.timestep
        a = self.mars.get_coords()
        b = self.phobos.get_coords()
        
        return a, b
    #anitmate function to update middle of circle         
    def animate(self, i):
        a,b = self.update()
        self.patches[0].center = a
        self.patches[1].center = b
        return self.patches
    
    #method to run the simulation
    def run(self, mars, phobos):
        fig = plt.figure()
        ax = plt.axes()
        
        self.patches = []
        
        self.patches.append(plt.Circle(self.mars.get_coords(), 300000, color = "r", animated = True))
        self.patches.append(plt.Circle(self.phobos.get_coords(), 300000, color = "b", animated = True))
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])
            
        ax.axis('scaled')
        ax.set_xlim(-12.3773e6, 12.3773e6)
        ax.set_ylim(-12.3773e6, 12.3773e6)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        self.anim = FuncAnimation(fig, self.animate, frames = self.N, repeat = False, interval = 50, blit = True)
        
        plt.show()