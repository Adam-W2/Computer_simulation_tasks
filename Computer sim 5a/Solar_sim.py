"""
Solar system - simulation class

"""
class Simulation(object):
    
    def __init__(self, timestep, N):
        self.timestep = timestep
        self.N = N
        self.planet_list = []
        
    def read_file(self):
        filein = open("Planets.txt", "r")
        for line in filein.readlines():
            temp = line.split(",")
            temp2 = Planet(temp[0], temp[1], temp[2], np.array((temp[3], temp[4])))
    def step_forward(self):
        
    def calc_acceleration(self, body):
        r = []
        
        for i in range(len(planet_list)):
            for j in range(len(planet_list)):
                if j != i:
                    
        