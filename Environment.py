import gym
import numpy as np
import matplotlib.pyplot as plt
import math
from PriorityQueue import PriorityQueue

class MoonEnvironment(gym.Env):
    def __init__(self, X, Y, elevation,grid_size,max_slope): #add more arguments later maybe
        super().__init__()

        self.X = X
        self.Y = Y
        self.elevation = elevation
        self.grid_size = grid_size
        self.max_slope = max_slope

        #Initial position = base, Goal1 = Big crater. It works with indices.
        self.initial_position = tuple([len(self.X)//2, len(self.Y)//2])
        """"
        TODO: We have to change the goal position to the big crater, and add the rest
        """
        self.goal1_position = tuple([22*len(self.X)//30, 18*len(self.Y)//30])
        self.state = self.initial_position        

        self.NEIGHBOR_OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, down, up

        # Possible actions: 5
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Tuple((gym.spaces.Discrete(len(self.X)), gym.spaces.Discrete(len(self.Y))))

    def elevation_cost(self, from_a, to_b):
        return abs(self.elevation[from_a[0], from_a[1]] - self.elevation[to_b[0], to_b[1]])
    
    def slope(self, from_a, to_b, ):
        distance = self.grid_size
        return math.degrees(math.atan((self.elevation[from_a[0], from_a[1]] - self.elevation[to_b[0], to_b[1]])/distance))
    
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
            return self.state, -100, done, {}  # large negative reward for invalid move
        elif self.state == self.goal1_position:
            done = True
        else:
            reward = -1 - elevation_cost
        if done:
            reward = self.goal_reached_score()
        """TODO: Add rewards and extra conditions"""
        return self.state, reward, done, {}

    def goal_reached_score(self):
        return 1000000000000000
    
    def neighbors(self, node):
        x, y = node
        max_x, max_y = len(self.X) - 1, len(self.Y) - 1
        neighbors = [(x + dx, y + dy) for dx, dy in self.NEIGHBOR_OFFSETS
                     if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y]
        neighbors = [n for n in neighbors if self.slope(node,n) <= float(self.max_slope)]
        return neighbors
    
    def reset(self):
        self.state = self.initial_position
        return self.state
    
    def render(self, path = None,came_from = None):
        plt.imshow(self.elevation, cmap='Spectral', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal1_position, color='green')
        plt.pause(0.001)  # pause a bit so that plots are updated

        if path is not None:
            path_x, path_y = zip(*path)
            plt.plot(path_x, path_y, 'r-')  # Plot the best path in red
        plt.show()

# ----------------- A* ALGORITHM ----------------------------

    def heuristic(self, from_a, to_b):
        return abs(from_a[0] - to_b[0]) + abs(from_a[1] - to_b[1])

    def astar(self, start, goal):
        start = tuple(start)
        goal = tuple(goal)
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {start: 0}
        goal_reached = False  
        all_nodes = set()  # keep track of all nodes visited
    
        while not frontier.empty():
            current = frontier.get()
            all_nodes.add(tuple(current))  # Add current node to all_nodes
    
            if current == goal and not goal_reached:
                goal_reached = True
                break
    
            for next in self.neighbors(current):
                next = tuple(next)
                current = tuple(current)
                if next in all_nodes:
                    continue
                new_cost = cost_so_far[current] + self.elevation_cost(current, next)
                if next == goal:
                    new_cost -= self.goal_reached_score()
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next,priority)
                    came_from[next] = current
            
            #self.live_render(None, came_from)

        if not goal_reached:
            #print("Goal not reachable!")
            return None, None, None
    
        # Reconstruct the path
        path = []
        current = goal  # Start from the goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # Add the start node to the path
        path.reverse()  
    
        return path, cost_so_far[goal], came_from 
    
    def live_render(self, path=None, came_from=None):
        plt.imshow(self.elevation, cmap='Spectral', origin='lower')
        plt.scatter(*self.state, color='red')
        plt.scatter(*self.goal1_position, color='green')
        plt.clf()
        if came_from is not None:
            for node, parent in came_from.items():
                plt.plot([node[0], parent[0]], [node[1], parent[1]], color = 'gray')

        if path is not None:
            path_x, path_y = zip(*path)
            plt.plot(path_x, path_y, 'r-')  # Plot the best path in red
        
        plt.draw()
        plt.pause(0.01)
    
