# import datetime
# import time, requests
# import pandas as pd
#
# import random
# import decimal
#
# import pandas as pd
# import googlemaps #pip install googlemaps
# import ast #pip install ast
# import math
#
# API_KEY = "AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs"
#
# map_client = googlemaps.Client(API_KEY)
#
# # assigned regular string date
# # date_time = datetime.datetime(2022, 8, 14, 0, 0)
#
# # print regular python date&time
# # print("date_time =>", date_time)
# #
# # # displaying unix timestamp after conversion
# # print("unix_timestamp => ",
# #       int((time.mktime(date_time.timetuple()))))
#
# def conv(date):
#     format = '%Y-%m-%d %H:%M:%S+05:30'
#     date_time = datetime.datetime.strptime(date, format)
#     ans = int((time.mktime(date_time.timetuple())))
#     return ans
# import cv2
#
# # print(conv('2022/08/14/20:20'))
# # def data_request_coord(x, y, t):
# #     # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
# #     # appid = {APIkey}
# #
# #     response = requests.get(
# #         "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=" + str(x) + "&lon=" + str(y) + "&dt=" + str(t) + "&appid=" + "2f24e1c60f207f07a58ece1a29433a73")
# #     data = response.json()
# #     print(data)
# #     print("Temp: " + str(round(data['data'][0]['temp'] - 273.15, 2)) + "C")
# #
# # data_request_coord(30.4598, 78.0944,int(time.mktime(date_time.timetuple())))
# # data_request_coord(53.631611, -113.323975,int(1660573938))
#
#
# df = pd.read_csv("test.csv")
#
# df = pd.DataFrame(df)
#
# for j in range(264):
#     print(j)
#     # # if(i<=150):
#     # #     continue    #26.0
#     # # if(j>10):
#     # #     break
#     # x = df.at[j, 'lat']
#     # y = df.at[j, 'long']
#     #
#     # f = open('static.png', 'wb')
#     # f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center=' + str(x) + ',' + str(y) + '&zoom=10&size=1000x1000&maptype=terrain&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off').content)
#     # f.close()
#     #
#     # from PIL import Image
#     # import numpy as np
#     # from matplotlib import pyplot as plt
#     #
#     # # Load image, ensure not palettised, and make into Numpy array
#     # pim = Image.open('static.png').convert('RGB')
#     # im = np.array(pim)
#     #
#     # # Define the blue colour we want to find - PIL uses RGB ordering
#     # blue = [156, 192, 249]
#     # # blue = [115, 139, 119]
#     # blue2 = [138, 180, 248]
#     # blue3 = [137, 181, 247]
#     # blue4 = [155, 191, 247]
#     #
#     # # Get X and Y coordinates of all blue pixels
#     # Y1, X1 = np.where(np.all(im == blue, axis=2))
#     # Y2, X2 = np.where(np.all(im == blue2, axis=2))
#     # Y3, X3 = np.where(np.all(im == blue3, axis=2))
#     # Y4, X4 = np.where(np.all(im == blue4, axis=2))
#     #
#     # Y = np.concatenate((Y1, Y2, Y3, Y4), axis=0)
#     # X = np.concatenate((X1, X2, X3, X4), axis=0)
#     #
#     # # print(X1,Y1)
#     # # print(X2,Y2)
#     # # print(X3,Y3)
#     # # print(X4,Y4)
#     #
#     # # im = plt.imread("static.png")
#     # # implot = plt.imshow(im)
#     # # for p,q in zip(X,Y):
#     # #     x_cord = p # try this change (p and q are already the coordinates)
#     # #     y_cord = q
#     # #     plt.scatter([x_cord], [y_cord])
#     # #     print(x_cord,y_cord)
#     # # plt.show()
#     #
#     # # print(X.shape,Y.shape)
#     # (h, w) = im.shape[:2]
#     # # print( w//2, h// 2)
#     # min = 100
#     # xfinal = 0
#     # yfinal = 0
#     # x1 = 0
#     #
#     # for i in range(X.shape[0]):
#     #     # print(i)
#     #     x1 = w // 2
#     #     x2 = X[i]
#     #     y1 = h // 2
#     #     y2 = Y[i]
#     #     dist = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
#     #     if (dist < min):
#     #         min = dist
#     #         xfinal = X[i]
#     #         yfinal = Y[i]
#     #     # print(x2,y2)
#     #
#     # print(str(min))
#     # df.at[j, 'river'] = 0
#     #
#     if(j%5!=0):
#         continue
#     min = float(decimal.Decimal(random.randrange(5000, 25000))/1000)
#     print(min)
#     df.at[j, 'data'] = min
#
#
# print(df)
#
# df.to_csv('test.csv')


