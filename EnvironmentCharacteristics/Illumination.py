import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

im = iio.imread('.//Media//Illumination.png')
av = np.average(im, axis=2)
av = av/256

plt.imshow(av)


av_lp = np.gradient(np.gradient(av))
