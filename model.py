import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import Adam, SGD, RMSprop, Adadelta, Adagrad, Adamax, Nadam, Ftrl
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.wrappers.scikit_learn import KerasClassifier
from math import floor
from sklearn.metrics import make_scorer, accuracy_score
# from bayes_opt import BayesianOptimization
from sklearn.model_selection import StratifiedKFold
from keras.layers import LeakyReLU
LeakyReLU = LeakyReLU(alpha=0.1)
import warnings
import joblib
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None)

data = pd.read_csv("last.csv")
# data = data.drop(['Unnamed: 0'],axis=1)
data = pd.get_dummies(data,columns =['weather'])
X = data.drop('class',axis =1)
y = data['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
joblib.dump(X_train.columns, "columns.pkl")

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
joblib.dump(sc, "std_scaler.pkl")
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Flatten, LeakyReLU, BatchNormalization, Dropout
from keras.activations import relu, sigmoid

from keras.layers import Dense, BatchNormalization, Dropout
import keras
from keras import regularizers


model = Sequential()

model.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'selu', input_dim = X_train.shape[1]))
model.add(BatchNormalization())
model.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'selu',kernel_regularizer=regularizers.l1(0.0001)))
model.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'selu'))
model.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'selu'))
model.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'selu',kernel_regularizer=regularizers.l1(0.0001)))
model.add(Dropout(0.2))

model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

es = EarlyStopping(monitor='accuracy', mode='max', verbose=0, patience=4)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, callbacks=es)

model.save('saved_model/my_model')