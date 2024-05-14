from stl import mesh
import matplotlib.pyplot as plt
from import_map import import_map_mesh, plot_grid
from environment import MoonEnvironment
import keyboard
import pygame

# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path (mesh is 297x297 km)
M = mesh.Mesh.from_file(aitor)
grid_size = 50000


X,Y,elevation = import_map_mesh(M,grid_size)

#plt.contourf(X, Y, elevation)
#plt.colorbar()
#plt.show()

#print(Y)
#plot_grid(X,Y,elevation)
#print(env.map)
env = MoonEnvironment(X,Y,elevation)

while True:
    plt.contourf(X, Y, elevation)
    plt.colorbar()
    env.step(index = int(input("Enter a number: ")))
    plt.scatter(env.state[0], env.state[1], c='red')
    plt.scatter(env.goal_position[0], env.goal_position[1], c='purple')
    plt.show()