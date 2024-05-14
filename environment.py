import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import keyboard
import pygame

class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation): #add arguments
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation
        self.initial_position = [self.X[-1][len(self.X)//2], self.Y[len(self.Y)//2][-1]]
        self.goal_position = [self.X[-1][4*len(self.X)//6], self.Y[4*len(self.Y)//6][-1]]

        #Create map
        self.map = np.array([self.X, self.Y])
        self.map_size = self.map.shape

        #Initialize state
        self.state = np.array(self.initial_position)
        self.traces = []   
        
        #Possible actions: 8
        self.action_space = gym.spaces.Discrete(8)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(self.map_size[1]), gym.spaces.Discrete(self.map_size[2])))

        pygame.init()
        self.cell_size = 1
        self.screen = pygame.display.set_mode((self.map_size[1]*self.cell_size, self.map_size[2]*self.cell_size))
    
    def reset(self):
        self.state = np.array(self.initial_position)
        self.traces = []
        return self.state

    def step(self,index):
        #Update
        self.state = self.next_state(self.state,index)
        self.traces.append(self.state)

    def next_state(self,state,index):
        transitions = {
            0: [0, +1],
            1: [+1, +1],
            2: [-1, +1],
            3: [0, 0],
            4: [-1, 0],
            5: [+1, 0],
            6: [-1, -1],
            7: [0, -1],
            8: [+1, -1]
        }
        if index in transitions:
            new_state = state + transitions[index]
            return new_state
        else:
            pass
        #For now all moves are valid