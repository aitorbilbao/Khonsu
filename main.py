from stl import mesh
import matplotlib.pyplot as plt
from import_map import import_map_mesh, plot_grid
from env_my import MoonEnvironment
from astar import a_star_search, reconstruct_path

import keyboard
import pygame

# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path (mesh is 297x297 km)
M = mesh.Mesh.from_file(aitor)
grid_size = 10000


X,Y,elevation = import_map_mesh(M,grid_size)



#pygame.init()
#self.cell_size = 1
#self.screen = pygame.display.set_mode((self.map_size[1]*self.cell_size, self.map_size[2]*self.cell_size))
#print(Y)
#plot_grid(X,Y,elevation)
#print(env.map)
#plt.contourf(X, Y, elevation)
#plt.colorbar()
#plt.show()

# ---------------------------------------------------------


# Create an instance of the environment
env = MoonEnvironment(X, Y, elevation)

# Perform the A* search
came_from, cost_so_far = a_star_search(env, env.initial_position, env.goal1_position)

# Reconstruct the path
path = reconstruct_path(came_from, env.initial_position, env.goal1_position)

# Print the path
print(path)