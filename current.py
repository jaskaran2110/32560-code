import datetime
import time, requests,json
import argparse
from decimal import *

parser = argparse.ArgumentParser()
parser.add_argument("val")
args=parser.parse_args()

a=args.val
b=a.split(',')

x= Decimal(b[0].strip())
y= Decimal(b[1].strip())

# print(x,y)
x = float(b[0].strip())
y = float(b[1].strip())


response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=" + str(x) + "&lon=" + str(y) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
data = response.json()
# print(data)

weather =  data['weather'][0]['main']
temp = (round(data['main']['temp'] - 273.15, 2))
pres = (round(data['main']['pressure'], 2))
hum = (round(data['main']['humidity'], 2))
speed = (round(data['wind']['speed'], 2))
clouds = (round(data['clouds']['all'], 2))

ans = {"size": 3, "data" : [{"latitude": x, "longitude": y, "weather": str(weather),
                  "temp": temp, "pressure": pres, "humidity": hum,"speed": speed
                     , "clouds": clouds}] }

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=" + str(x+0.09) + "&lon=" + str(y+0.9) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
data = response.json()
# print(data)

weather =  data['weather'][0]['main']
temp = (round(data['main']['temp'] - 273.15, 2))
pres = (round(data['main']['pressure'], 2))
hum = (round(data['main']['humidity'], 2))
speed = (round(data['wind']['speed'], 2))
clouds = (round(data['clouds']['all'], 2))

ans["data"].append({"latitude": x+0.09, "longitude": y+0.09, "weather": str(weather),
                  "temp": temp, "pressure": pres, "humidity": hum,"speed": speed
                     , "clouds": clouds})

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=" + str(x-0.09) + "&lon=" + str(y+0.09) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
data = response.json()
# print(data)

weather =  data['weather'][0]['main']
temp = (round(data['main']['temp'] - 273.15, 2))
pres = (round(data['main']['pressure'], 2))
hum = (round(data['main']['humidity'], 2))
speed = (round(data['wind']['speed'], 2))
clouds = (round(data['clouds']['all'], 2))

ans["data"].append({"latitude": x-0.09, "longitude": y+0.09, "weather": str(weather),
                  "temp": temp, "pressure": pres, "humidity": hum,"speed": speed
                     , "clouds": clouds})




jsonString = json.dumps(ans, indent=4)
print(jsonString)