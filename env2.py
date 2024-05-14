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
        self.initial_position = [len(self.X)//2, len(self.Y)//2]
        self.goal_position = [4*len(self.X)//6, 4*len(self.Y)//6]
        self.state = self.initial_position
        
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(len(self.X)), gym.spaces.Discrete(len(self.Y))))

    def step(self, action):
        if action == 0 and self.state< self.Y[-1][-1]:  # up
            self.state[1] += 1
        elif action == 1 and self.state[1] > 0:  # down
            self.state[1] -= 1
        elif action == 2 and self.state[0] > 0:  # left
            self.state[0] -= 1
        elif action == 3 and self.state[0]<self.X[-1][-1]:  # right
            self.state[0] += 1
    
        done = self.state == self.goal_position
        return np.array(self.state), 0.0, done, {}
    
    def reset(self):
        self.state = self.initial_position
        return np.array(self.state)
    
    def render(self):
        plt.imshow(self.elevation, cmap='Spectral', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal_position, color='green')
        plt.pause(0.001)  # pause a bit so that plots are updated