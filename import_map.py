import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Download the STL file and load it into a mesh
aitor = "C://Users//aitor//Desktop//Path AI//map.stl"
# jan = 

#Change file path
M = mesh.Mesh.from_file(aitor)

def import_map_mesh(mesh_path):

    X = []
    Y = []
    Z = []

    '''
    # Plot the 3D mesh
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(M.vectors))

    # Auto scale to the mesh size
    scale = M.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()
    '''
    # Extract the coordinates from the mesh
    for vector in M.vectors:
        for vertex in vector:
            X.append(vertex[0])
            Y.append(vertex[1])
            Z.append(vertex[2])

    # Define the new grid size
    new_grid_size = 50000

    # Generate the new grid points
    x_min, x_max = min(X), max(X)
    y_min, y_max = min(Y), max(Y)
    new_x_grid = numpy.arange(x_min, x_max, new_grid_size)
    new_y_grid = numpy.arange(y_min, y_max, new_grid_size)
    new_xx, new_yy = numpy.meshgrid(new_x_grid, new_y_grid)

    # Calculate the average height for each new grid region
    new_z_grid = numpy.zeros_like(new_xx)
    for i in range(len(new_x_grid)-1):
        for j in range(len(new_y_grid)-1):
            region_mask = (X >= new_x_grid[i]) & (X < new_x_grid[i+1]) & (Y >= new_y_grid[j]) & (Y < new_y_grid[j+1])
            if numpy.any(region_mask):
                new_z_grid[j, i] = numpy.mean(numpy.array(Z)[region_mask])
    return new_xx, new_yy, new_z_grid

def plot_grid(new_xx, new_yy, new_z_grid):
    # Create a new plot for 3D grid visualization
    figure = pyplot.figure()
    axes = figure.add_subplot(projection='3d')


    # Plot the new grid
    axes.plot_surface(new_xx, new_yy, new_z_grid, cmap='Spectral')

    # Show the plot to the screen
    pyplot.show()