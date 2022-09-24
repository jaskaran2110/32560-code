import datetime
import time, requests
import pandas as pd
import json,sys
import subprocess
# assigned regular string date
# date_time = datetime.datetime(2022, 8, 14, 0, 0)

# print regular python date&time
# print("date_time =>", date_time)
#
# # displaying unix timestamp after conversion
# print("unix_timestamp => ",
#       int((time.mktime(date_time.timetuple()))))

def conv(date):
    format = '%Y-%m-%d %H:%M:%S+05:30'
    date_time = datetime.datetime.strptime(date, format)
    ans = int((time.mktime(date_time.timetuple())))
    return ans
import cv2

# print(conv('2022/08/14/20:20'))
# def data_request_coord(x, y, t):
#     # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
#     # appid = {APIkey}
#
#     response = requests.get(
#         "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=" + str(x) + "&lon=" + str(y) + "&dt=" + str(t) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
#     data = response.json()
#     print(data)
#     print("Temp: " + str(round(data['data'][0]['temp'] - 273.15, 2)) + "C")

# data_request_coord(30.4598, 78.0944,int(time.mktime(date_time.timetuple())))
# data_request_coord(53.631611, -113.323975,int(1660573938))


# df = pd.read_csv("prev.csv")
#
# df = pd.DataFrame(df)
#
# for i, row in df.iterrows():
#     print(i)
#     # if (i>5):
#     #     break
#     x = df.at[i, 'lat']
#     y = df.at[i, 'long']
#     t = conv(str(df.at[i, 'dt_txt']) )
#     # print(x, y, t)
#     response = requests.get(
#         "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=" + str(x) + "&lon=" + str(y) + "&dt=" + str(t) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
#     data = response.json()
#     # print(data)
#     #
#     # df.at[i, 'temp'] = str(round(data['data'][0]['temp'] - 273.15, 2))
#     # df.at[i, 'humidity'] = str(round(data['data'][0]['humidity'], 2))
#     # df.at[i, 'wind'] = str(round(data['data'][0]['wind_speed'], 2))
#     # df.at[i, 'cloud'] = str(round(data['data'][0]['clouds'], 2))
#     df.at[i, 'weather'] = data['data'][0]['weather'][0]['main']
#     # df.at[i, 'pressure'] = data['data'][0]['pressure']
#
#
#
# print(df)
#
# df.to_csv('median.csv')



from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv("New_data2.csv")

df = pd.DataFrame(df)

for i, row in df.iterrows():
    print(i)
    # if(i<=150):
    #     continue    #26.0
    if(i<35):
        continue
    # if(i<=25):
    #     continue
    latitude = df.at[i, 'Latitude']
    longitude = df.at[i, 'Longitude']

    data, _ = subprocess.Popen([sys.executable, "current.py", str(latitude) + "," + str(longitude)],
                               stdout=subprocess.PIPE).communicate()
    jsonString = json.loads(data)

    x = subprocess.Popen([sys.executable, "dist.py", str(latitude) + "," + str(longitude)],
                         stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    jsonString["data"][0].update({"riverDistance": float(x)})


    e = subprocess.Popen([sys.executable, "elevation.py", str(latitude) + "," + str(longitude)],
                         stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    jsonString["data"][0].update({"seaLevel": float(e)})

    s = subprocess.Popen([sys.executable, "slope.py", str(latitude) + "," + str(longitude)],
                         stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    # jsonString["data"][0].update({"slope": float(s)})

    jsonString["data"][0].update({"road": 80})

    f = subprocess.Popen([sys.executable, "forest.py", str(latitude) + "," + str(longitude)],
                         stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    jsonString["data"][0].update({"forest": float(f)})

    m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][0])],
                         stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    jsonString["data"][0].update({"class": str(m)})

    df.at[i,'sea level'] =   jsonString["data"][0]['seaLevel']
    df.at[i,'weather'] =   jsonString["data"][0]['weather']
    df.at[i,'pressure'] =   jsonString["data"][0]['pressure']
    df.at[i,'clouds'] =   jsonString["data"][0]['clouds']
    df.at[i,'river'] =   jsonString["data"][0]['riverDistance']
    df.at[i,'forest'] =   jsonString["data"][0]['forest']

    df.at[i,'class'] =   jsonString["data"][0]['class']
    df.at[i,'angle'] =   s

print(df)

df.to_csv('median.csv')















