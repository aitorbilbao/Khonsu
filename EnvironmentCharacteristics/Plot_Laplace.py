from Import_files import *
import matplotlib.pyplot as plt


fig, ax = plt.subplots(2,5)
#------- Increase contrast ---------
for index, image in enumerate(Image_edge_list):
    p1, p99 = np.percentile(image, (1, 99))
    image = np.clip((image - p1) / (p99 - p1), 0, 1)
    if index < 5:
        ax[0][index].imshow(image, cmap='magma', alpha=1)
    if index >= 5:
        ax[1][index-5].imshow(image, cmap='gray', alpha=1)


# ----- Plot saved discretised data -----

plt.imshow(stretched_imp, cmap='gray',alpha = 1)
plt.show()


'''
# Resize the images to the same size
stretched_ima_resized = cv2.resize(stretched_ima, (test_grid_flipped.shape[1], test_grid_flipped.shape[0]))

# Combine the images by adding them together
combined_image = cv2.addWeighted(stretched_ima_resized, 0.5, stretched_imp, 0.5, 0)

# Display the combined image
plt.imshow(combined_image, cmap='gray')
plt.show()
'''

