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

        # Create map
        self.map = np.array(elevation)
        self.map_size = self.map.shape

        # Initialize state
        self.state = np.array(self.initial_position)
        self.traces = []   

        # Possible actions: 8
        self.action_space = gym.spaces.Discrete(8)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(self.map_size[0]), gym.spaces.Discrete(self.map_size[1])))

    def reset(self):
        self.state = np.array(self.initial_position)
        self.traces = []
        return self.state

    def step(self, action):
        # Define actions
        transitions = {
            0: [0, +1],  # N
            1: [+1, +1], # NE
            2: [-1, +1], # NW
            3: [0, 0],   # 0 (idle)
            4: [-1, 0],  # W
            5: [+1, 0],  # E
            6: [-1, -1], # SW
            7: [0, -1],  # S
            8: [+1, -1]  # SE
        }

        # Calculate new state
        if action in transitions:
            new_state = self.state + transitions[action]
            new_state = np.clip(new_state, [0, 0], [self.map_size[0]-1, self.map_size[1]-1])

            # Calculate reward
            reward = -1  # Default reward for a step
            if np.array_equal(new_state, self.goal_position):
                reward = 100  # Reward for reaching the goal
                done = True
            else:
                done = False

            self.state = new_state
            self.traces.append(self.state)

            return self.state, reward, done, {}
        else:
            raise ValueError("Invalid action")

    def render(self, mode='human'):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.map, cmap='gray', origin='lower', interpolation='none')
        plt.scatter(self.initial_position[1], self.initial_position[0], color='blue', label='Start')
        plt.scatter(self.goal_position[1], self.goal_position[0], color='red', label='Goal')
        if self.traces:
            trace = np.array(self.traces)
            plt.plot(trace[:, 1], trace[:, 0], color='green', label='Path')
        plt.legend()
        plt.show()
