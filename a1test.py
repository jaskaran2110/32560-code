import Image
import colorsys
import numpy as np
from matplotlib import pyplot as plt

import cv2
img = cv2.imread('static.png')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# pim = Image.open('static.png')
# pim = pim.convert(mode="HSV")

def HSVColor(img):
    if isinstance(img,Image.Image):
        r,g,b = img.split()
        Hdat = []
        Sdat = []
        Vdat = []
        for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
            h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

a = Image.open('static.png')
b = HSVColor(a)
b.show("Image")
cv2.imshow("hello",hsvImg)
cv2.waitKey(0)