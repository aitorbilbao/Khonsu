import gym
import numpy as np
import matplotlib.pyplot as plt

from import_map import M, import_map_mesh

X,Y,elevation = import_map_mesh(M)

class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation): #add arguments
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation
