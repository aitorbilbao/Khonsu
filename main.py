from stl import mesh
from import_map import import_map_mesh, plot_grid


# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path
M = mesh.Mesh.from_file(aitor)
grid_size = 50000


X,Y,elevation = import_map_mesh(M,grid_size)
plot_grid(X,Y,elevation)