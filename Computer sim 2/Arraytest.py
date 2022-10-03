"""
Test class for the class RadioactiveDecay
"""
from Array import RadioactiveDecay

class TestArray(object):
    def test(self):
        N = int(input("Please input size of square matrix, e.g N = 10 for a 10 x 10: "))
        L = float(input("Please input the decay constant: "))
        T = float(input("Please input timestep: "))
        V = RadioactiveDecay(N, L, T) #values required to create object array
        V.createArray() #creates array
        V.decay() #decays array

def main():
    run = TestArray() #runs method test to run program
    run.test()
    
main()