import math
import utm
import googlemaps #pip install googlemaps
API_KEY = "AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs"
import ast
map_client = googlemaps.Client(API_KEY)
import json

import argparse
from decimal import *

parser = argparse.ArgumentParser()
parser.add_argument("val")
args=parser.parse_args()

a=args.val
b=a.split(',')


# print(x,y)
lat1 = float(b[0].strip())
long1 = float(b[1].strip())


u = utm.from_latlon(lat1, long1)
x1 = u[0]
y1 = u[1]

sum_slope = 0.0
location = lat1,long1
response = map_client.elevation(location)
response_no_brackets = ast.literal_eval((str(response)[1:-1]))
pure_elevation = response_no_brackets["elevation"]
z1 = math.ceil(pure_elevation*100)/100

import cmath

def calc(count, radius, center):
    x, y = center
    for i in range(count):
        r = cmath.rect(radius, (2*cmath.pi)*(i/count))
        yield [round(x+r.real, 6), round(y+r.imag, 6)]

ans = list(calc(8, 0.001, [lat1, long1]))

for i in range(8):
    lat2 = ans[i][0]
    long2 = ans[i][1]
    u2 = utm.from_latlon(lat2, long2)
    x2 = u2[0]
    y2 = u2[1]
    location = lat2, long2
    response = map_client.elevation(location)
    response_no_brackets = ast.literal_eval((str(response)[1:-1]))
    pure_elevation = response_no_brackets["elevation"]
    z2 = math.ceil(pure_elevation * 100) / 100
    # print(z2, x2, y2)
    slope = math.degrees(math.atan((z2 - z1) / ((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5)))
    sum_slope += slope

avg = sum_slope/8.0

print("%.3f" % avg)
