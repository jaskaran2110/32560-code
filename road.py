
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

import requests

url = "https://roads.googleapis.com/v1/nearestRoads?points="+str(x)+"%2C"+str(y)+"%7C"+str(x+0.01)+"%2C" +str(y+0.01)+"%7C"+str(x+0.02)+"%2C" +str(y+0.02)+"%7C"+str(x+0.03)+"%2C" +str(y+0.03)+"%7C"+str(x-0.02)+"%2C" +str(y-0.02)+"&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

print(response.text)

# data["snappedPoints"]
import json
unique_stuff = { each['originalIndex'] : each for each in data["snappedPoints"] }.values()
# data = json.dumps(list(unique_stuff))
# data = json.loads(data)

r = json.dumps(list(unique_stuff))
unique_stuff = json.loads(r)
print(type(unique_stuff["snappedPoints"]))