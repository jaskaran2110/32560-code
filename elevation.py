from pprint import pprint #pip install pprint
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

API_KEY = "AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs"

map_client = googlemaps.Client(API_KEY)

location = x,y


#Creates an elevation list
response = map_client.elevation(location)

#Converting the list into a dictionary
response_no_brackets = ast.literal_eval((str(response)[1:-1]))

pure_elevation = response_no_brackets["elevation"] #outputs a float like 139.9674987792969
output_elevation = str(math.ceil(pure_elevation*100)/100) #Ceiling function rounds up to 2 decimal points -> 139.97

print(str(output_elevation))