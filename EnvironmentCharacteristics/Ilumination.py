from EnvironmentCharacteristics.Import_files import Image_list,X, Y, elevation, test_grid,grid_size
import numpy
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

def Illumination():
    Illumination = Image_list[0]
    resized_array = numpy.resize(Illumination, elevation.shape)
    filtered_array = gaussian_filter(resized_array, sigma=1)
    scaled_array = (filtered_array - numpy.min(filtered_array)) / (numpy.max(filtered_array) - numpy.min(filtered_array))

    plt.imshow(scaled_array, cmap='gray')
    plt.savefig('EnvironmentCharacteristics//Illumination.png')
