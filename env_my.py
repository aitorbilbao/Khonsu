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
        #Initial position = base, Goal1 = Big crater. It works with indices.
        self.initial_position = [len(self.X)//2, len(self.Y)//2]
        """"
        TODO: We have to change the goal position to the big crater, and add the rest
        """
        self.goal1_position = [4*len(self.X)//6, 4*len(self.Y)//6]
        self.state = self.initial_position
        
        # Possible actions: 5
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(len(self.X)), gym.spaces.Discrete(len(self.Y))))

    def cost(self, a, b):
        return abs(self.elevation[a[0], a[1]] - self.elevation[b[0], b[1]])
    
    def step(self, action):
        self.old_state = self.state
        if action == 0 and self.state[1] < len(self.Y)-1:  # up
            self.state[1] += 1
        elif action == 1 and self.state[1] > 0:  # down
            self.state[1] -= 1
        elif action == 2 and self.state[0] > 0:  # left
            self.state[0] -= 1
        elif action == 3 and self.state[0] < len(self.X)-1:  # right
            self.state[0] += 1
        elif action == 4:  # stay still
            pass
        
        if self.state == self.old_state:
            return np.array(self.state), -100, False, {}  # large negative reward for invalid move

        #Elevation cost (going down is good, going up is bad)
        elevation_cost = self.cost(self.old_state, self.state)
        
        done = self.state == self.goal1_position
        reward = -1 - elevation_cost
        if done:
            reward = 1000000000
        """TODO: Add rewards and extra conditions"""
        return np.array(self.state), reward, done, {}
    
    def neighbors(self, node):
        neighbors = []
        x, y = node
        if x > 0: neighbors.append((x-1, y))  # left
        if x < len(self.X)-1: neighbors.append((x+1, y))  # right
        if y > 0: neighbors.append((x, y-1))  # down
        if y < len(self.Y)-1: neighbors.append((x, y+1))  # up
        return neighbors
    
    def reset(self):
        self.state = self.initial_position
        return np.array(self.state)
    
    def render(self):
        plt.imshow(self.elevation, cmap='terrain', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal1_position, color='green')
        plt.pause(0.001)  # pause a bit so that plots are updated