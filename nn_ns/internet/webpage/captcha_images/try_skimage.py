
import skimage.morphology
import skimage.filters
import skimage.filters.rank
import skimage.io
import matplotlib.pyplot as plt
import skimage.restoration # denoise_wavelet, cycle_spin
import numpy # bool_

class Global:
    image_path = '0_67uguw.jpg'


noisy_image = skimage.io.imread(Global.image_path)
#http://scikit-image.org/docs/stable/auto_examples/filters/plot_cycle_spinning.html#sphx-glr-auto-examples-filters-plot-cycle-spinning-py
#image = skimage.restoration.denoise_wavelet(noisy_image)
image = skimage.restoration.cycle_spin(noisy_image, func=skimage.restoration.denoise_wavelet, max_shifts=7)
assert image.size == 12500
assert image.shape == (50, 250) # (height, width)
#image.dtype is uint8

#error: binary_image = skimage.filters.threshold_local(image, 15, 'mean')
MEAN = image.mean(); MAX = image.max(); MIN = image.min()
threshold = (0.05-0.5)/0.5 * (MAX-MEAN) + MEAN
assert MIN <= threshold <= MEAN <= MAX





def my_thin_denoise(binary_image):
    assert type(binary_image[0][0]) is numpy.bool_
    N = 1; L=1+2*N; NN = L*L*9/16.0
    old = binary_image
    binary_image = old.copy()
    height, width = binary_image.shape
    for i in range(N, height-N):
      for j in range(N, width-N):
        square_LL = old[i-N:i+N+1, j-N:j+N+1]
        assert square_LL.shape == (L, L)
        S = sum(sum(square_LL))
        if S < NN:
            binary_image[i][j] = False
        else:
            binary_image[i][j] = True
    return binary_image

binary_image = image < threshold
skimage.io.imshow(binary_image); plt.show()

old_binary_image = binary_image
binary_image = my_thin_denoise(binary_image)
skimage.io.imshow(binary_image); plt.show()


x = binary_image[20:35, 45:60]
import pytesseract
pytesseract.image_to_string(x)



# http://scikit-image.org/docs/stable/auto_examples/edges/plot_skeleton.html#sphx-glr-auto-examples-edges-plot-skeleton-py
image_skeleton = skimage.morphology.skeletonize(binary_image)
image_thin = skimage.morphology.thin(binary_image)
skel, distance = skimage.morphology.medial_axis(binary_image, return_distance=True)
#skimage.io.imshow(image_skeleton)
#skimage.io.imshow(image_thin)


from skimage.util.colormap import magma

fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(binary_image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_title('original')
ax[0].axis('off')

ax[1].imshow(distance*skel, cmap=magma, interpolation='nearest')
ax[1].contour(binary_image, [0.5], colors='w')
ax[1].set_title('medial_axis')
ax[1].axis('off')

ax[2].imshow(image_skeleton, cmap=plt.cm.gray, interpolation='nearest')
ax[2].set_title('skeletonize')
ax[2].axis('off')

ax[3].imshow(image_thin, cmap=plt.cm.gray, interpolation='nearest')
ax[3].set_title('thin')
ax[3].axis('off')

fig.tight_layout()
plt.show()












