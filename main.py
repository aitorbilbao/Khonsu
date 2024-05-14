from stl import mesh
import matplotlib.pyplot as plt
from import_map import import_map_mesh, plot_grid
from environment import MoonEnvironment

# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path (mesh is 297x297 km)
M = mesh.Mesh.from_file(aitor)
grid_size = 10000


X,Y,elevation = import_map_mesh(M,grid_size)

#plt.contourf(X, Y, elevation)
#plt.colorbar()
#plt.show()

#print(Y)
#plot_grid(X,Y,elevation)
#env = MoonEnvironment(X,Y,elevation)
#print(env.map)
