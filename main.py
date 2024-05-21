from ImportMesh import X,Y,elevation,grid_size
from Environment import MoonEnvironment
from RoverSpecs import RoverSpecifications

# ----------------- ROVER SPECS ----------------------------

Rover = RoverSpecifications()
max_slope = Rover.max_slope

# ------------- A STAR ALGORITHM ----------------------------

env = MoonEnvironment(X, Y, elevation,grid_size,max_slope)

start = env.initial_position
goal = env.goal1_position

path, cost, came_from = env.astar(start, goal)
env.render(path,came_from)