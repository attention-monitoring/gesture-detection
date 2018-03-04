import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import linalg as LA

fname = 'nikitahand.png'
image = Image.open(fname).convert("L")
img_arr = np.asarray(image)
plt.imshow(img_arr, cmap='gray')

img_size = img_arr.shape
print(img_size)

list1 = [50, 100, 150, 200, 250]
point1 = [50,50]

#for i in list:
#   for j in list:
x = 100
y = 100

for i in range(1, 500):
        list8 = [img_arr[x+1,y+1], img_arr[x-1,y-1],img_arr[x+1,y],img_arr[x-1,y],img_arr[x,y+1],img_arr[x,y-1],img_arr[x-1,y+1],img_arr[x+1,y-1]];
        print(list8)
        print(max(list8))
        index8 = list8.index(max(list8));
        print index8
        if index8 == 1 or index8 == 3 or index8 == 7:
            x=x-1
        if index8 == 0 or index8 == 2 or index8 == 6:
            x=x+1
        if index8 == 1 or index8 == 5 or index8 == 6:
            y=y-1
        if index8 == 0 or index8 == 4 or index8 == 7:
            y=y+1
print()
print(x)
print(y)
plt.show()
