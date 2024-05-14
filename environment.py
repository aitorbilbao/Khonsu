import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import keyboard

class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation, live_display=False, render_trace=False): #add arguments
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation
        self.initial_position = [self.X[-1][len(self.X)//2], self.Y[len(self.Y)//2][-1]]

        #Create map
        self.map = np.array([self.X, self.Y])
        self.map_size = self.map.shape

        #Initialize state
        self.state = np.array(self.initial_position)
        self.traces = [self.state]   
        
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