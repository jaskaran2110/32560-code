
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

# f=open('static.png','wb')
# # f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=12&size=600x600&maptype=transit&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off&style=feature:landscape.natural.landcover|color:0x00ff00|visibility:on').content)
# f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=12&size=300x300&maptype=transit&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off').content)
# f.close()

r = requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=12&size=300x300&maptype=transit&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off')
f = open('test2.png', 'wb')
f.write(r.content)
f.close()

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


green = (206, 234, 214)
# green3 = (206, 234, 214)
green2 = (0,254,0)
import cv2
img = cv2.imread('test2.png')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# pim = Image.open('static.png').convert('HSV')
# hsvImg  = np.array(pim)
# print(hsvImg[5,5])

# im = Image.open("static.png")
# rgb_im = im.convert(mode="HSV")
height, width = hsvImg.shape[:2]
# pixArray = im.load()
colorPixCount = 0


for y in range(0, height):
    for x in range(0, width):  # Iterate over every X coordinate on a given Y coordinate
        # print(rgb_im.getpixel((x,y)))
        if hsvImg[x,y][0] >=55 and hsvImg[x,y][0] <=70 and hsvImg[x,y][1] >=14  and hsvImg[x,y][1] <=67 and hsvImg[x,y][2] >=202 and hsvImg[x,y][2] <= 239:
            colorPixCount += 1
                # print(x_cord,y_cord)

# rgb_im.show()
# print(colorPixCount)
# print(width*height)
cover = colorPixCount/(width*height)*100
print("%.3f" % cover)