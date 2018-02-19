import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from skimage import feature
import numpy as np


image = Image.open('face.png').convert("L")
face_arr = np.asarray(image)
plt.imshow(face_arr, cmap='gray')
# plt.show()

image = Image.open('hand.png').convert("L")
hand_arr = np.asarray(image)
plt.imshow(hand_arr, cmap='gray')
# plt.show()

# import the necessary packages


class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        # store the number of points and radius
        self.numPoints = numPoints
        self.radius = radius

    def describe(self, image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(image, self.numPoints,
                                           self.radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(),
                                 bins=np.arange(0, self.numPoints + 3),
                                 range=(0, self.numPoints + 2))

        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        # return the histogram of Local Binary Patterns
        return hist
