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

    def elevation_cost(self, from_a, to_b):
        return abs(self.elevation[from_a[0], from_a[1]] - self.elevation[to_b[0], to_b[1]])
    
    def step(self, action):
        done = False
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
        #Elevation cost
        elevation_cost = self.elevation_cost(self.old_state, self.state)

        if self.state == self.old_state:
            return np.array(self.state), -100, done, {}  # large negative reward for invalid move
        elif self.state == self.goal1_position:
            done = True
        else:
            reward = -1 - elevation_cost/10
        if done:
            reward = 1000000000000000
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
    
    def render(self, path = None,came_from = None):
        plt.imshow(self.elevation, cmap='terrain', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal1_position, color='green')
        plt.pause(0.001)  # pause a bit so that plots are updated

        self.plot(path, came_from)

        plt.show()

# ----------------- A* ALGORITHM ----------------------------
    def heuristic(self, from_a, to_b):
        return abs(from_a[0] - to_b[0]) + abs(from_a[1] - to_b[1])

    def astar(self, start, goal):
        frontier = [] #Priority queue storing nodes to be explored
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {tuple(start): 0}
        goal_reached = False  # Add a flag to track if the goal is reached
        all_nodes = set()  # Keep track of all nodes visited
    
        while frontier:
            current = heapq.heappop(frontier)[1]
            print(f"Current node: {current}, Cost so far: {cost_so_far[tuple(current)]}")
            all_nodes.add(tuple(current))  # Add current node to all_nodes
    
            # Don't break when the goal is found, but update the flag and continue exploring
            if current == tuple(goal) and not goal_reached:
                goal_reached = True
                print("Goal reached!")
                break
    
            for next in self.neighbors(current):
                new_cost = cost_so_far[tuple(current)] + self.elevation_cost(current, next)
                if next == tuple(goal):
                    new_cost -= 1000
                print(f"Neighbor: {next}, New cost: {new_cost}")
                next_tuple = tuple(next)
                if next_tuple not in cost_so_far or new_cost < cost_so_far[next_tuple]:
                    cost_so_far[next_tuple] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next_tuple] = tuple(current)
                    print(f"Adding node to frontier: {next}, Priority: {priority}")
    
        # If the goal was not reached, return None or an appropriate value
        if not goal_reached:
            print("Goal not reachable!")
            return None, None, None
    
        # Reconstruct the path
        path = []
        current = tuple(goal)  # Start from the goal
        while current != tuple(start):
            path.append(current)
            current = came_from[current]
        path.append(tuple(start))  # Add the start node to the path
        path.reverse()  # Reverse the path to start-to-goal order
    
        return path, cost_so_far[tuple(goal)], came_from  # Return the path, its cost, and all nodes visited
    
    # In your plotting function, use the returned all_nodes to plot all paths and path to plot the best path
    def plot(self, path=None, came_from=None):
        if path is not None:
            path_x, path_y = zip(*path)
            plt.plot(path_x, path_y, 'r-')  # Plot the best path in red
    
        plt.show()
    
