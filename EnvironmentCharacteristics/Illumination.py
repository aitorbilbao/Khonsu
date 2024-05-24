import imageio.v3 as iio
import numpy as np
'''
from ImportMesh import M
import matplotlib.pyplot as plt
'''

im = iio.imread('.//Media//Illumination.png')
av = np.average(im, axis=2)
av = av/256

print(im.shape)
'''
x_coordinates = M.vectors[:, 0]
print(M.vectors[0])

y_coordinates = M.vectors[:, 1]
z_coordinates = M.vectors[:, 2]

plt.tricontourf(x_coordinates, y_coordinates, z_coordinates, cmap='Spectral')
plt.colorbar()
plt.show()


av_lp = np.gradient(np.gradient(av))
real_lp = np.gradient(np.gradient(M))
'''