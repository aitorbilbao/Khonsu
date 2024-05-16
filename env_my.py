import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import keyboard
import pygame
import heapq

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

    def cost(self, from_a, to_b):
        return abs(self.elevation[from_a[0], from_a[1]] - self.elevation[to_b[0], to_b[1]])
    
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

        #Elevation cost
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
    
    def render(self, path = None):
        plt.imshow(self.elevation, cmap='terrain', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal1_position, color='green')
        plt.pause(0.001)  # pause a bit so that plots are updated

        # If a path is provided, plot it on top of the environment
        if path is not None:
            path_x, path_y = zip(*path)
            plt.plot(path_x, path_y, 'r-')

        plt.show()

# ----------------- A* ALGORITHM ----------------------------
    def heuristic(env, from_a, to_b):
        return abs(from_a[0] - to_b[0]) + abs(from_a[1] - to_b[1])

    def astar(env, start, goal):
        frontier = [] #Priotity queue storing nodes to be explored
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {tuple(start): 0}

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for next in env.neighbors(current):
                new_cost = cost_so_far[tuple(current)] + env.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + env.heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        # Reconstruct the path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()  # Reverse the path to start-to-goal order

            return path, cost_so_far[goal]  # Return the path and its cost