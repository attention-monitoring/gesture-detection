import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import linalg as LA
from matplotlib import pyplot as plt

fname = 'nikitaface.png'
image = Image.open(fname).convert("L")
img_arr = np.asarray(image)
plt.imshow(img_arr, cmap='gray')

img_size = img_arr.shape
r3 = int(img_size[0]/3);
c3 = int(img_size[1]/3);

face1 = img_arr[:r3, :c3]
face2 = img_arr[:r3, c3+1:2*c3]
face3 = img_arr[:r3, 2*c3+1:]
face4 = img_arr[r3+1:2*r3, :c3]
face5 = img_arr[r3+1:2*r3, c3+1:2*c3]
face6 = img_arr[r3+1:2*r3, 2*c3+1:]
face7 = img_arr[2*r3+1:, :c3]
face8 = img_arr[2*r3+1:, c3+1:2*c3]
face9 = img_arr[2*r3+1:, 2*c3+1:]

count1 = 0;
count2 = 0;
count3 = 0;
count4 = 0;
count5 = 0;
count6 = 0;
count7 = 0;
count8 = 0;
count9 = 0;

for i in range(0,r3-1):
    for j in range(0,c3-1):
        if face1[i,j] >150:
            count1= count1 +1
        if(face2[i,j])>150:
            count2= count2 +1
        if(face3[i,j])>150:
            count3= count3 +1
        if(face4[i,j])>150:
            count4= count4 +1
        if(face5[i,j])>150:
            count5= count5 +1
        if(face6[i,j])>150:
            count6= count6 +1
        if(face7[i,j])>150:
            count7= count7 +1
        if(face8[i,j])>150:
            count8= count8 +1
        if(face9[i,j])>150:
            count9= count9 +1

print count1, count2, count3, count4, count5, count6, count7, count8, count9

fname = 'nikitahand.png'
image = Image.open(fname).convert("L")
img_arr = np.asarray(image)
plt.imshow(img_arr, cmap='gray')

img_size = img_arr.shape
r3 = int(img_size[0]/3);
c3 = int(img_size[1]/3);

face1 = img_arr[:r3, :c3]
face2 = img_arr[:r3, c3+1:2*c3]
face3 = img_arr[:r3, 2*c3+1:]
face4 = img_arr[r3+1:2*r3, :c3]
face5 = img_arr[r3+1:2*r3, c3+1:2*c3]
face6 = img_arr[r3+1:2*r3, 2*c3+1:]
face7 = img_arr[2*r3+1:, :c3]
face8 = img_arr[2*r3+1:, c3+1:2*c3]
face9 = img_arr[2*r3+1:, 2*c3+1:]

count11 = 0;
count21 = 0;
count31 = 0;
count41 = 0;
count51 = 0;
count61 = 0;
count71 = 0;
count81 = 0;
count91 = 0;

for i in range(0,r3-1):
    for j in range(0,c3-1):
        if face1[i,j] >150:
            count11= count11 +1
        if(face2[i,j])>150:
            count21= count21 +1
        if(face3[i,j])>150:
            count31= count31 +1
        if(face4[i,j])>150:
            count41= count41 +1
        if(face5[i,j])>150:
            count51= count51 +1
        if(face6[i,j])>150:
            count61= count61 +1
        if(face7[i,j])>150:
            count71= count71 +1
        if(face8[i,j])>150:
            count81= count81 +1
        if(face9[i,j])>150:
            count91= count91 +1

print count1-count11,count2-count21,count3-count31,count4-count41,count5-count51,count6-count61,count7-count71,count8-count81,count9-count91,
