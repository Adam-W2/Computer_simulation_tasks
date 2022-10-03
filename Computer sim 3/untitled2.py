# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:15:47 2022

@author: damsk
"""

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SineAnimation1(object):

    def __init__(self):
        # set initial and final x coordinates of circle
        self.xpos = 0.0
        self.xmax = 2*math.pi
        
        # set simulation parameters
        self.niter = 500
        self.xincr = (self.xmax - self.xpos)/self.niter

    def init(self):
        # initialiser for animator
        return self.patch,

    def animate(self, i):
        # update the position of the circle
        self.xpos += self.xincr
        self.patch.center = (self.xpos, math.sin(self.xpos))
        return self.patch,

    def run(self):
        # create plot elements
        fig = plt.figure()
        ax = plt.axes()

        # create circle of radius 0.1 centred at initial coordinates and add to axes
        self.patch = plt.Circle((self.xpos, math.sin(self.xpos)), 0.1, color = 'g', animated = True)
        ax.add_patch(self.patch)

        # set up the axes
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(-1.1, 1.1)
        ax.set_xlabel('x (rads)')
        ax.set_ylabel('sin(x)')

        # create the animator
        self.anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 50, blit = True)

        # show the plot
        plt.show()



def main():
    s = SineAnimation1()
    s.run()
    
main()





        

    
    