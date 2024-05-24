import numpy
#from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def import_map_mesh(M,new_grid_size):

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
    
    #here
    # print([i for i in X if i])
    # print(numpy.min([i for i in X if i]))
    dx = numpy.min([i for i in X if i])
    dy = numpy.min([i for i in Y if i])
    new_X = [int(i) for i in X/dx]
    new_Y = [int(i) for i in Y/dx]
    test_grid = numpy.zeros((numpy.max(new_X)+1,numpy.max(new_Y)+1))
    print(numpy.array(Z).shape)
    Z_compelete = numpy.vstack((numpy.array(new_X),numpy.array(new_Y),numpy.array(Z))).T
    for i in Z_compelete:
        test_grid[int(i[0])][int(i[1])] = i[-1]
        if int(i[1])==452:
            print(test_grid[int(i[0])][int(i[1])])
    
    # Plot the test grid
    pyplot.imshow(test_grid, cmap='magma')
    pyplot.colorbar()
    pyplot.show()





    # Generate the new grid points
    x_min, x_max = min(X), max(X)
    y_min, y_max = min(Y), max(Y)
    new_x_grid = numpy.arange(x_min, x_max, new_grid_size)
    new_y_grid = numpy.arange(y_min, y_max, new_grid_size)
    new_xx, new_yy = numpy.meshgrid(new_x_grid, new_y_grid)

    #Get average heights
    new_elevation = average_value(X, Y, Z, new_x_grid, new_y_grid, new_xx, new_yy)
    return new_xx, new_yy, new_elevation

def average_value(X, Y, Z, new_x_grid, new_y_grid, new_xx, new_yy):
    # Calculate the average height for each new grid region
    new_z_grid = numpy.zeros_like(new_xx)
    for i in range(len(new_x_grid)-1):
        for j in range(len(new_y_grid)-1):
            region_mask = (X >= new_x_grid[i]) & (X < new_x_grid[i+1]) & (Y >= new_y_grid[j]) & (Y < new_y_grid[j+1])
            if numpy.any(region_mask):
                new_z_grid[j, i] = numpy.mean(numpy.array(Z)[region_mask])
    for i in range(len(new_x_grid)-1):
        region_mask = (X >= new_x_grid[i]) & (X < new_x_grid[i+1]) & (Y >= new_y_grid[-1])
        if numpy.any(region_mask):
            new_z_grid[-1, i] = numpy.mean(numpy.array(Z)[region_mask])
    for j in range(len(new_y_grid)-1):
        region_mask = (X >= new_x_grid[-1]) & (Y >= new_y_grid[j]) & (Y < new_y_grid[j+1])
        if numpy.any(region_mask):
            new_z_grid[j, -1] = numpy.mean(numpy.array(Z)[region_mask])
    region_mask = (X >= new_x_grid[-1]) & (Y >= new_y_grid[-1])
    if numpy.any(region_mask):
        new_z_grid[-1, -1] = numpy.mean(numpy.array(Z)[region_mask])

    return new_z_grid

def plot_grid(new_xx, new_yy, new_z_grid):
    # Create a new plot for 3D grid visualization
    figure = pyplot.figure()
    axes = figure.add_subplot(projection='3d')


    # Plot the new grid
    axes.plot_surface(new_xx, new_yy, new_z_grid, cmap='Spectral')

    # Show the plot to the screen
    pyplot.show()