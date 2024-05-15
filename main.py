from stl import mesh
import matplotlib.pyplot as plt
from import_map import import_map_mesh, plot_grid
from env_my import MoonEnvironment
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


import numpy as np

# Create an instance of the environment
env = MoonEnvironment(X, Y, elevation)

# Reset the environment and get the initial state
state = env.reset()

# Run an episode
done = False
while not done:
    # Select an action
    action = np.random.choice(env.action_space.n)  # random policy
    # Take a step in the environment
    state, reward, done, info = env.step(action)
    # Render the environment
    env.render()