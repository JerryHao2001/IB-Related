from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from sklearn.model_selection import  train_test_split
from keras import backend as k
import matplotlib.pyplot as plt
import numpy as np

'''
path='./mnist.npz'  
f = np.load(path) 
x_train, y_train = f['x_train'], f['y_train']  
x_test, y_test = f['x_test'], f['y_test'] 
f.close()
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size = 0.2)
'''
 
img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

if k.image_data_format() == 'channels_first':
    x_train = x_train.reshape(-1, 1, img_rows, img_cols)
    x_test = x_test.reshape(-1, 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_train = x_train.astype('float32')

category = 10
y_train = keras.utils.to_categorical(y_train,category)
y_test = keras.utils.to_categorical(y_test,category)
batch_size = 128
num_epoch = 10

def network(x_train, y_train,batch_size,num_epoch):
    global category,input_shape
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(category, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

    result = model.fit(x_train, y_train, batch_size=batch_size, epochs=num_epoch, verbose=1, validation_data=(x_test, y_test))

    return result,model

def evaluate(model):
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

result,model = network(x_train,y_train,batch_size,num_epoch)
evaluate(model)