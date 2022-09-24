import pandas as pd
import numpy as np
import joblib,json
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import tensorflow as tf

import argparse
from decimal import *

parser = argparse.ArgumentParser()
parser.add_argument("val")
args=parser.parse_args()

a=args.val
# print(a)
# b=a.split(',')
a = a.replace("'", "\"")
# print(a)
stud_obj = json.loads(a)


# print(type(stud_obj))
weather = str(stud_obj["weather"])
river = float(stud_obj["riverDistance"])
sea = float(stud_obj["seaLevel"])
temp = float(stud_obj["temp"])
speed = float(stud_obj["speed"])
pressure = float(stud_obj["pressure"])
forest = float(stud_obj["forest"])
humidity = float(stud_obj["humidity"])
cloud = float(stud_obj["clouds"])


# print(weather)
# print(str(river))
# print(str(sea))
# print(str(temp))
# print(str(speed))
# print(str(pressure))



def clean_data(df_x):
    df_x = pd.get_dummies(data = df_x,  columns=["weather"], drop_first = False)
    return df_x
def standardize_data(dta):
    scaler = joblib.load("std_scaler.pkl")
    X_transformed = scaler.transform(dta)
    return X_transformed

data = {'weather':weather,'river':river,'sea level':sea,'temp':temp,'humidity':humidity, 'forest':forest,'wind':speed,'pressure':pressure, 'cloud':cloud}

df_input = pd.DataFrame.from_records([data], )

main_cols = joblib.load("columns.pkl")
sample_df = pd.DataFrame(columns = main_cols)
clean_df = clean_data(df_input)
main_df = sample_df.append(clean_df)
main_df = main_df.fillna(0)

# print(main_df)
# print(sample_df)

new_model = tf.keras.models.load_model('saved_model/my_model')

std_df = standardize_data(main_df)
pre = new_model.predict(std_df,verbose=0)

if(pre[0][0]>=0.5):
    print("Flood")
else:
    print("Non-Flood")

