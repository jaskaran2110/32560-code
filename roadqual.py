import os
import cv2

data_dir = "sih_road_dataset"
labels = ["good", "poor", "satisfactory", "very_poor"]
x = []
y = []
for label in labels:
    print(label)
    data = os.path.join(data_dir, label)
    for image in os.listdir(data):
        try:
            im = cv2.imread(os.path.join(data, image), cv2.IMREAD_COLOR)
            im = cv2.resize(im, (224, 224))
            # Using the Canny filter with different parameters

            x.append(im)
            y.append(labels.index(label))


        except Exception as e:
            pass
import numpy as np

x = np.array(x)/255.0
y = np.array(y)



x = x.reshape(-1, 224, 224, 3)

y = y.reshape(-1, 1)

from tensorflow.keras.utils import to_categorical

y = to_categorical(y,4,)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagenerator = ImageDataGenerator(
fill_mode= 'nearest',
horizontal_flip=False,
vertical_flip=False,
shear_range=0.1,
zoom_range = 0.1, # Randomly zoom image
width_shift_range=0.2,  # randomly shift images horizontally (fraction of total width)
height_shift_range=0.2
)
datagenerator.fit(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y)

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (5, 5), padding='same', strides=(2, 2), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (5, 5), padding='same', strides=(2, 2), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (5, 5), padding='same', strides=(2, 2), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (5, 5), padding='same', strides=(2, 2), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Dense(4, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

earlystop = tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=4,restore_best_weights=True)

model.fit(datagenerator.flow(x_train,y_train,batch_size=32),epochs=20,callbacks=[earlystop],validation_data=datagenerator.flow(x_test,y_test))

import pandas as pd
history = pd.DataFrame(model.history.history)
history[["loss", "val_loss"]].plot()

model.save('saved_model2/road')