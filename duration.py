import datetime
import time, requests,json
import pandas as pd
import argparse
from decimal import *
df = pd.read_csv("prev.csv")

def conv(date):
    format = '%Y-%m-%d %H:%M:%S+05:30'
    date_time = datetime.datetime.strptime(date, format)
    ans = int((time.mktime(date_time.timetuple())))
    return ans

df = pd.DataFrame(df)

for i, row in df.iterrows():
    print(i)
    x = df.at[i, 'latitude']
    y = df.at[i, 'longitude']
    t = df.at[i, 'dt_txt']
    t = conv(str(t))
    response = requests.get(
        "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=" + str(x) + "&lon=" + str(y) + "&dt=" + str(t) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
    data = response.json()
    counter = 0
    weather = data['data'][0]['weather'][0]['main']
    while( weather=='Snow' or weather=='Rain'):
        counter = counter +1
        t = t + 86400
        response = requests.get(
            "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=" + str(x) + "&lon=" + str(
                y) + "&dt=" + str(t) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
        data = response.json()
        weather = data['data'][0]['weather'][0]['main']

    print(counter)
    df.at[i, 'duration'] = counter

print(df)
df.to_csv('median.csv')

