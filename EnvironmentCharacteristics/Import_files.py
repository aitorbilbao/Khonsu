import imageio.v3 as iio
import numpy as np
import scipy.ndimage as ndimage
import cv2
import pickle



#----- Download media --------
illumination = iio.imread('.//Media//1_Illumination.png')
PWEH = iio.imread('.//Media//2_PolarWaterEquivalentHydrogen.png')
Olivine = iio.imread('.//Media//3_Olivine.png')
Plagioclase = iio.imread('.//Media//4_Plagioclase.png')
HCP = iio.imread('.//Media//5_HighCalciumPyroxene.png')
CrustalThickness = iio.imread('.//Media//6_CrustalThickness.png')
Height = iio.imread('.//Media//7_TerrainHeight.png')
PSR = iio.imread('.//Media//8_PSR.png')


# ----- Transform into array -------

Image_1 = np.average(illumination, axis=2)
Image_2 = np.average(PWEH, axis=2)
Image_3 = np.average(Olivine, axis=2)
Image_4 = np.average(Plagioclase,axis =2)
Image_5 = np.average(HCP, axis=2)
Image_6 = np.average(CrustalThickness, axis=2)
Image_7 = np.average(Height, axis=2)
Image_8 = np.average(PSR, axis=2)

Image_list = [Image_1,Image_2,Image_3,Image_4,Image_5,Image_6,Image_7,Image_8]

#--------- Normalize -----------------

for image in Image_list:
    image = image/256

#--------- Laplace Operator ---------------
Image_edge_list = []

for image in Image_list:
    Image_edge_list. append(ndimage.laplace(image))

file = ".//Mesh//discretized_data.pkl"
with open(file, 'rb') as f:
        X, Y, elevation, test_grid,grid_size = pickle.load(f)


imp = ndimage.laplace(test_grid)
p1_,p99_ = np.percentile(imp, (1, 99))
stretched_imp = np.clip((imp - p1_) / (p99_ - p1_), 0, 1)