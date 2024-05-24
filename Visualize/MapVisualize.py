import pickle
from matplotlib import pyplot

# ------- Import Discretized Data and Test Grid -------

file = ".//Mesh//discretized_data.pkl"
with open(file, 'rb') as f:
        X, Y, elevation, test_grid = pickle.load(f)

def elevation_map(test_grid):
    pyplot.imshow(test_grid, cmap='magma')
    pyplot.colorbar()
    pyplot.show()

def plot_grid(X, Y, elevation):
    figure = pyplot.figure()
    axes = figure.add_subplot(projection='3d')
    axes.plot_surface(X, Y, elevation, cmap='Spectral')
    pyplot.show()

