import gym
import numpy as np

from import_map import M, import_map_mesh

X,Y,elevation = import_map_mesh(M)

class MoonEnvironment(gym.Env):
    def __init__(self): #add arguments
        super().__init__()



