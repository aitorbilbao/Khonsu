import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import pickle

def Jing():
    file = ".//Mesh//discretized_data.pkl"
    with open(file, 'rb') as f:
            X, Y, elevation, test_grid,grid_size = pickle.load(f)

    FeO = iio.imread('.//Media//feo abundance.png')
    image = np.average(FeO, axis=2)
    image = image/256
    resized_array = np.resize(image, elevation.shape)
    filtered_array = gaussian_filter(resized_array, sigma=1)
    #scaled_array = (filtered_array - np.min(filtered_array)) / (np.max(filtered_array) - np.min(filtered_array))

    plt.imshow(filtered_array, cmap='gray')
    plt.savefig('EnvironmentCharacteristics//FeO.png')
    plt.show()
