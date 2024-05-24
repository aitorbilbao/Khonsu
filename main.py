<<<<<<< HEAD
#from Mesh.ImportMesh import X,Y,elevation,grid_size
=======
from ImportMesh import X,Y,elevation,grid_size
>>>>>>> 6212916d9e2b47ed67369a0cd2868881cb1582c0
from Environment import MoonEnvironment
from Agent.RoverSpecs import RoverSpecifications

# ----------------- ROVER SPECS ---------------------------

Rover = RoverSpecifications()
#max_slope = Rover.max_slope
max_slope = 50

# ----------------- Environment ---------------------------

env = MoonEnvironment(X, Y, elevation,grid_size,max_slope)

start = env.initial_position
goal = env.goal1_position

# --------------- A STAR ALGORITHM -------------------------

#path, cost, came_from = env.astar(start, goal)
#env.render(path,came_from)
