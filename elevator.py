
import pandas as pd
import googlemaps #pip install googlemaps
import ast #pip install ast
import math

API_KEY = "AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs"

map_client = googlemaps.Client(API_KEY)

df = {
    "latitude": [14.5398,32.8353,26.4816,21.1495,25.6339],
    "longitude": [75.0937,76.9103,82.8434,86.7154,84.0726]
    # "sealevel" : []
}
# read_file = pd.read_excel ('Sea level.xlsx')
# read_file.to_csv ('sea.csv', index = None, header=True)

df = pd.read_csv("test.csv")

df = pd.DataFrame(df)

for i, row in df.iterrows():
    location = df.at[i,'latitude'] ,df.at[i,'longitude']
    response = map_client.elevation(location)

    # Converting the list into a dictionary
    response_no_brackets = ast.literal_eval((str(response)[1:-1]))

    pure_elevation = response_no_brackets["elevation"]  # outputs a float like 139.9674987792969
    output_elevation = math.ceil(pure_elevation * 100) / 100 # Ceiling function rounds up to 2 decimal points -> 139.97


    df.at[i,'sea level'] =   output_elevation
    print(i)

print(df)

df.to_csv('testans.csv')
