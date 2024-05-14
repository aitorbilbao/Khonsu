import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation, live_display=False, render_trace=False): #add arguments
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation

        self.render_trace = render_trace
        self.traces = []    
        self.live_display = live_display


        #Create map
        self.map = np.array([self.X, self.Y])
        self.map_size = self.map.shape

        #forward, diagonal (2), sides (2), idle (1)
        self.action_space = gym.spaces.Discrete(6)
        self.all_actions = list(range(self.action_space.n))

        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(self.map_size[1]), gym.spaces.Discrete(self.map_size[2])))

        #Initialize state
        self.state = None

        #Color map: order is free space, wall, agent, goal
        self.cmap = colors.ListedColormap(['red','black', 'white', 'green'])
        self.bounds = [0, 1, 2, 3, 4, 5]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

        #for generating videos
        self.ax_imgs = []

        self.EMPTY = 0
        self.WALL = 1
        self.AGENT = 2
        self.GOAL = 3


    def reset(self):
        #Reset to base
        initial_position = [self.X[-1][len(self.X[-1]) // 2], self.Y[-1][len(self.Y[-1]) // 2]]
        self.state = np.array(initial_position)
        return self.state
    
    
    def step(self, action):
        old_state = self.state

        if action == 0: #Move forward
            x =+ 1
        elif action == 1: #Move diagonally to the right
            x =+ 1
            y =+ 1
        elif action == 2: #Move diagonally to the left
            x =+ 1
            y =- 1
        elif action == 3: #Move to the right
            y =+ 1
        elif action == 4: #Move to the left
            y =- 1
        elif action == 5: #Stand still
            pass


        

        