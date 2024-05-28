import numpy

def import_map_mesh(M,new_grid_size):

    X = []
    Y = []
    Z = []

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
#    print(numpy.array(Z).shape)
    Z_compelete = numpy.vstack((numpy.array(new_X),numpy.array(new_Y),numpy.array(Z))).T
    for i in Z_compelete:
        test_grid[int(i[1])][int(i[0])] = i[-1]
#        if int(i[1])==452:
#            print(test_grid[int(i[0])][int(i[1])])
    
    test_grid = numpy.flip(test_grid, axis=0)
    for i in range(len(test_grid)):
        for j in range(len(test_grid[i])):
            if test_grid[i][j] == 0:
                test_grid[i][j] =(test_grid[i][j+1]+test_grid[i][j-1])/2

    # Generate the new grid points
    x_min, x_max = min(X), max(X)
    y_min, y_max = min(Y), max(Y)
    new_x_grid = numpy.arange(x_min, x_max, new_grid_size)
    new_y_grid = numpy.arange(y_min, y_max, new_grid_size)
    new_xx, new_yy = numpy.meshgrid(new_x_grid, new_y_grid)

    #Get average heights
    new_elevation = average_value(X, Y, Z, new_x_grid, new_y_grid, new_xx, new_yy)
    return new_xx, new_yy, new_elevation, test_grid

    
    


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