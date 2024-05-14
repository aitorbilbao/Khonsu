import gym
import numpy as np
import matplotlib.pyplot as plt

class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation): #add arguments
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation
        self.map = np.array([self.X, self.Y])
        self.map_size = self.map.shape
        #frente, diagonal (2), lados (2), parado (1)
        self.action_space = gym.spaces.Discrete(6)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(self.map_size[1]), gym.spaces.Discrete(self.map_size[2])))

        #Initialize state
        self.state = None

    def reset(self):
        #Reset to base
        initial_position = [self.X[-1][len(self.X[-1]) // 2], self.Y[-1][len(self.Y[-1]) // 2]]
        self.state = np.array(initial_position)
        return self.state
    
    def step(self, action):
        x,y = self.state

        if action == 0: #Move forward
            x =+ 1
        

        