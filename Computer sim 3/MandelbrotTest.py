# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:04:23 2022

@author: damsk
"""

from Mandelbrot import Mandelbrot

class TestMandelbrot(object):
    def test(self):
        xrange = (-2.025, 0.6) #inputs for creating mandelbrot object
        yrange = (-1.125, 1.125)
        N = 800
        A = Mandelbrot(xrange, yrange, N)
        A.array()
        A.plot()
        
def main(): #main function to run code
    run = TestMandelbrot()
    run.test()

main()