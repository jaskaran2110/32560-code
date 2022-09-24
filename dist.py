
import requests
import googlemaps #pip install googlemaps
import ast #pip install ast
import math
import argparse
from decimal import *

parser = argparse.ArgumentParser()
parser.add_argument("val")
args=parser.parse_args()

a=args.val
b=a.split(',')

x= float(b[0].strip()) 
y= float(b[1].strip())

f=open('static.png','wb')
f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=10&size=1000x1000&maptype=terrain&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off').content)
f.close()

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


# Load image, ensure not palettised, and make into Numpy array
pim = Image.open('static.png').convert('RGB')
im  = np.array(pim)

# Define the blue colour we want to find - PIL uses RGB ordering
blue = [156, 192, 249]
# blue = [115, 139, 119]
blue2 = [138, 180, 248]
blue3 = [137, 181, 247]
blue4 = [155, 191, 247]

# Get X and Y coordinates of all blue pixels
Y1, X1 = np.where(np.all(im==blue,axis=2))
Y2, X2 = np.where(np.all(im==blue2,axis=2))
Y3, X3 = np.where(np.all(im==blue3,axis=2))
Y4, X4 = np.where(np.all(im==blue4,axis=2))

Y = np.concatenate((Y1 ,Y2,Y3,Y4),axis=0)
X = np.concatenate((X1 ,X2,X3,X4), axis=0)

# print(X1,Y1)
# print(X2,Y2)
# print(X3,Y3)
# print(X4,Y4)

# im = plt.imread("static.png")
# implot = plt.imshow(im)
# for p,q in zip(X,Y):
#     x_cord = p # try this change (p and q are already the coordinates)
#     y_cord = q
#     plt.scatter([x_cord], [y_cord])
#     print(x_cord,y_cord)
# plt.show()

# print(X.shape,Y.shape)

(h, w) = im.shape[:2]
# print( w//2, h// 2)
min = 250
xfinal = 0
yfinal = 0
x1 = 0

for i in range(X.shape[0]):
    # print(i)
    x1 = w // 2
    x2 = X[i]
    y1 = h // 2
    y2 = Y[i]
    dist = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    if (dist < min):
        min = dist
        xfinal = X[i]
        yfinal = Y[i]
    # print(x2,y2)

print(str("%.3f" % min))
# print(xfinal, yfinal)
# print((((x1 - xfinal) ** 2) + ((yfinal-x1) ** 2)) ** 0.5)

# print( "River distance is "+ str(((((x1 - xfinal) ** 2) + ((yfinal-y1) ** 2)) ** 0.5)/3.333))

# im = plt.imread("static.png")
# implot = plt.imshow(im)
# plt.scatter( [xfinal],[yfinal])
#
# plt.scatter([x1], [x1])
# plt.show()
#
