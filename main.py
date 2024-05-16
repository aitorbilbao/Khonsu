from stl import mesh
import matplotlib.pyplot as plt
from import_map import import_map_mesh, plot_grid
from env_my import MoonEnvironment

# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path (mesh is 297x297 km)
M = mesh.Mesh.from_file(aitor)
grid_size = 1000
X,Y,elevation = import_map_mesh(M,grid_size)

# ------------- A STAR ALGORITHM ----------------------------

env = MoonEnvironment(X, Y, elevation)

start = env.initial_position
goal = env.goal1_position

path, cost, came_from = env.astar(start, goal)
env.render(path,came_from)