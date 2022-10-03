"""
Solar system - Planet class

"""
import numpy as np

class Planet(object):
    def __init__(self, name, colour, mass, coords, velocity, acceleration):
        self.name = name
        self.mass = mass
        self.coords = coords
        self.velocity = velocity
        self.acceleration = acceleration
        self.prev_acceleration = np.array((0,0))
        self.timestep = 70
        self.colour = colour
        
    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_coords(self):
        return self.coords

    def get_velocity(self):
        return self.velocity
    
    def get_acceleration(self):
        return self.acceleration
    
    def get_prev_acceleration(self):
        return self.prev_acceleration

    def update_coords(self):
        self.coords = self.coords + self.velocity * self.timestep + 1/6 * (4 * self.acceleration - self.prev_acceleration) * (self.timestep)**2
    
    def update_velocity(self, new_acceleration):
        self.velocity = self.velocity + 1/6 * (2 * new_acceleration + 5 * self.acceleration - self.prev_acceleration) * self.timestep
    
    def set_coords(self,coords):
        self.coords = coords
        
    def set_velocity(self, velocity):
        self.velocity = velocity
    
    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

