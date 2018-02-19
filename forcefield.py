# Alrenate wat to convert to grey scale
# from scipy.misc import imread
# myimage = imread("person.jpg", True)
# print(myimage)



import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import linalg as LA
fname = 'person.jpg'
image = Image.open(fname).convert("L")
img_arr = np.asarray(image)
plt.imshow(img_arr, cmap='gray')
#plt.show()

img_size = img_arr.shape
print(img_size)
img_h = img_size[0]
img_w = img_size[1]
img_force = np.zeros(img_size)

#print(img_force)

distance = 0
force = np.zeros((2,1))
r = np.zeros((2,1))
offset = 12;
kernel = offset*2 + 1;

for y in range(offset+1,img_h-offset):
    for x in range(offset+1,img_w-offset):
        force = np.zeros((2,1))
        r = np.zeros((2,1))
        for yy in range(y-offset,y+offset):
            for xx in range(x-offset,x+offset):
                if (xx != x and yy != y):
                    r[0] = xx-x
                    r[1] = yy-y
                    force[0] = force[0] + (r[0]*(float(img_arr[yy,xx])/LA.norm(r)**3))
                    force[1] = force[1] + (r[1]*(float(img_arr[yy,xx])/LA.norm(r)**3))

        img_force[y,x] = LA.norm(force)

# % display the image (original and force field)
# img_force = uint8(img_force);
# figure(1); clf;
# imshow(img_force);

plt.imshow(img_force, cmap='gray')
plt.show()
