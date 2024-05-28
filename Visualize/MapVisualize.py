from matplotlib import pyplot

# ------- Import Discretized Data and Test Grid -------

def elevation_map(test_grid):
    pyplot.imshow(test_grid, cmap='magma')
    pyplot.colorbar()
    pyplot.show()

def plot_discretized_data(X, Y, elevation):
    pyplot.imshow(elevation, cmap='Spectral', origin='lower')
    pyplot.colorbar()
    pyplot.show()

def plot_grid(X, Y, elevation):
    figure = pyplot.figure()
    axes = figure.add_subplot(projection='3d')
    axes.plot_surface(X, Y, elevation, cmap='Spectral')
    pyplot.show()

def illumination():
     return 'hello'