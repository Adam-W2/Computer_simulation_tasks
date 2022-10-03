#!/bin/python3
# Planet class for Mars and Phobos simulation

class Planet:
    def __init__(self, name, mass, coords, velocity, acceleration ):
        self.name = name
        self.mass = mass
        self.coords = coords
        self.velocity = velocity
        self.acceleration = acceleration

    def __str__(self):
        return "Planet: (" + self.name + ", " + str(self.mass) + ", " + str(self.coords) + ", " + str(self.velocity) + ")"

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

    def set_coords(self, coords):
        self.coords = coords

    def set_velocity(self, velocity):
        self.velocity = velocity
    
    def set_acceleration(self, acceleration):
        self.acceleration = acceleration
