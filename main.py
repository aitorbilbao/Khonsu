from stl import mesh
import zipfile
from ImportMesh import import_map_mesh, plot_grid
from Environment import MoonEnvironment
from RoverSpecs import RoverSpecs
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(current_dir, "map.zip")

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extract('map.stl', current_dir)

max_slope = 30
#Change file path (mesh is 297x297 km)
M = mesh.Mesh.from_file(current_dir + '/map.stl')
grid_size = 50000
X,Y,elevation = import_map_mesh(M,grid_size)

# ------------- A STAR ALGORITHM ----------------------------

env = MoonEnvironment(X, Y, elevation,grid_size,max_slope)

start = env.initial_position
goal = env.goal1_position

path, cost, came_from = env.astar(start, goal)
env.render(path,came_from)