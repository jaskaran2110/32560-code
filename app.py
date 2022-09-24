import subprocess
import sys, random
from flask import Flask, request
from geopy.geocoders import Nominatim
import pandas as pd

import cv2
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# latitude =  17.72
# longitude = 82.37
import json

# latitude =  30.7333
# longitude = 76.7794
from PIL import Image
import numpy as np


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':

        latitude = 30.7333
        longitude = 76.7794

        geoLoc = Nominatim(user_agent="GetLoc")

        data, _ = subprocess.Popen([sys.executable, "current.py", str(latitude) + "," + str(longitude)],
                                   stdout=subprocess.PIPE).communicate()
        jsonString = json.loads(data)

        block, _ = subprocess.Popen([sys.executable, "tiff.py", str(latitude) + "," + str(longitude)],
                                    stdout=subprocess.PIPE).communicate()
        j = json.loads(block)

        jsonString.update(j)
        # print("current")
        x = subprocess.Popen([sys.executable, "dist.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"riverDistance": float(x)})

        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][0].update({"title": ans[0]})

        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][0].update({"road": n})
        f = subprocess.Popen([sys.executable, "forest.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][0])],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"class": str(m)})

        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][1].update({"title": ans[0]})

        x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"riverDistance": float(x)})
        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][1].update({"road": n})
        f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][1])],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"class": str(m)})

        x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"riverDistance": float(x)})
        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][2].update({"road": n})
        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][2].update({"title": ans[0]})

        f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test2.py"],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"class": str(m)})

        counter = False
        df = pd.read_csv("datas.csv")

        for index, row in df.iterrows():
            long = row['Longitude']
            lat = row['Latitude']
            latmin = lat - 0.04
            latmax = lat + 0.04
            longmin = long - 0.04
            longmax = long + 0.04

            if (latitude >= latmin and latitude <= latmax and longitude >= longmin and longitude <= longmax):
                counter = True
        jsonString["data"][0].update({"allow": counter})
        jsonString["data"][1].update({"allow": counter})
        jsonString["data"][2].update({"allow": counter})

        pr1 = float(random.randrange(8400, 9600)) / 100
        pr2 = float(random.randrange(8400, 9600)) / 100
        pr3 = float(random.randrange(8400, 9600)) / 100

        jsonString["data"][0].update({"pred": pr1})
        jsonString["data"][1].update({"pred": pr2})
        jsonString["data"][2].update({"pred": pr3})


        return jsonString

    else:
        output = request.get_json()

        latitude = float(output['latitude'])
        longitude = float(output['longitude'])

        geoLoc = Nominatim(user_agent="GetLoc")

        data, _ = subprocess.Popen([sys.executable, "current.py", str(latitude) + "," + str(longitude)],
                                   stdout=subprocess.PIPE).communicate()
        jsonString = json.loads(data)

        block, _ = subprocess.Popen([sys.executable, "tiff.py", str(latitude) + "," + str(longitude)],
                                    stdout=subprocess.PIPE).communicate()
        j = json.loads(block)

        jsonString.update(j)
        # print("current")
        x = subprocess.Popen([sys.executable, "dist.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"riverDistance": float(x)})

        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][0].update({"title": ans[0]})

        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][0].update({"road": n})
        f = subprocess.Popen([sys.executable, "forest.py", str(latitude) + "," + str(longitude)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][0])],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][0].update({"class": str(m)})

        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][1].update({"title": ans[0]})

        x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"riverDistance": float(x)})
        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][1].update({"road": n})
        f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][1])],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][1].update({"class": str(m)})

        x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"riverDistance": float(x)})
        # print("dist")
        e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"seaLevel": float(e)})

        s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"slope": float(s)})

        n = random.randint(0, 2)

        jsonString["data"][2].update({"road": n})
        locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))

        ans = locname.address.split(',')
        jsonString["data"][2].update({"title": ans[0]})

        f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"forest": float(f)})

        m = subprocess.Popen([sys.executable, "test2.py"],
                             stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        jsonString["data"][2].update({"class": str(m)})

        counter = False
        df = pd.read_csv("datas.csv")

        for index, row in df.iterrows():
            long = row['Longitude']
            lat = row['Latitude']
            latmin = lat - 0.04
            latmax = lat + 0.04
            longmin = long - 0.04
            longmax = long + 0.04

            if (latitude >= latmin and latitude <= latmax and longitude >= longmin and longitude <= longmax):
                counter = True
        jsonString["data"][0].update({"allow": counter})
        jsonString["data"][1].update({"allow": counter})
        jsonString["data"][2].update({"allow": counter})

        pr1 = float(random.randrange(8400, 9600)) / 100
        pr2 = float(random.randrange(8400, 9600)) / 100
        pr3 = float(random.randrange(8400, 9600)) / 100

        jsonString["data"][0].update({"pred": pr1})
        jsonString["data"][1].update({"pred": pr2})
        jsonString["data"][2].update({"pred": pr3})

        return jsonString


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2000)
