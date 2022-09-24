# 48.257848, 11.419932
import requests
import cv2
import numpy as np
import tensorflow as tf

x = 48.257848
y = 11.419932

# f=open('test.png','wb')
# # f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=12&size=600x600&maptype=transit&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off&style=feature:landscape.natural.landcover|color:0x00ff00|visibility:on').content)
# f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=19&size=300x300&maptype=satellite&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off').content)
# f.close()

r = requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+str(x)+','+str(y)+'&zoom=22&size=300x300&maptype=satellite&key=AIzaSyCk55griHhs0gHqb2plbt5AndtpOFN-uMs&format=png&style=feature:all|element:labels|visibility:off')

# wb mode is stand for write binary mode
f = open('asd.png', 'wb')

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()

model =  tf.keras.models.load_model('saved_model2/road')

from PIL import Image
def convert_to_array(img):
    im = cv2.imread(img)
    img = Image.fromarray(im, 'RGB')
    image = img.resize((224, 224))
    return np.array(image)
def get_profile_name(label):
    if label==0:
        return "Good"
    if label==1:
        return "Poor"
    if label==2:
        return "Satisfactory"
    if label==3:
        return "Very_Poor"

def predict_profile(file):
    print("Predicting .................................")
    ar=convert_to_array(file)
    ar=ar/255
    a=[]
    a.append(ar)
    a=np.array(a)
    score=model.predict(a,verbose=1)
    print(score)
    label_index=np.argmax(score)
    print(label_index)
    acc=np.max(score)
    profile=get_profile_name(label_index)
    print(profile)
    print("The predicted profile is a "+profile+" with accuracy =    "+str(acc))

predict_profile("asd.png")

