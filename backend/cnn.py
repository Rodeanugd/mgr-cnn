from imports import *
from keras.layers import Dropout

def TestModel(input_shape=(288, 432, 4), classes=10):
    X_input = Input(input_shape)

    X = Conv2D(8, kernel_size=(3, 3), strides=(1, 1))(X_input)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((2, 2))(X)

    X = Dropout(rate=0.15)(X)
    X = Conv2D(16, kernel_size=(3, 3), strides=(1, 1))(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((2, 2))(X)

    X = Dropout(rate=0.15)(X)
    X = Conv2D(32, kernel_size=(3, 3), strides=(1, 1))(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((2, 2))(X)

    X = Dropout(rate=0.15)(X)
    X = Conv2D(64, kernel_size=(3, 3), strides=(1, 1))(X)
    X = BatchNormalization(axis=-1)(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((2, 2))(X)

    X = Dropout(rate=0.15)(X)
    X = Conv2D(128, kernel_size=(3, 3), strides=(1, 1))(X)
    X = BatchNormalization(axis=-1)(X)
    X = Activation('relu')(X)
    X = MaxPooling2D((2, 2))(X)

    X = Flatten()(X)

    X = Dropout(rate=0.33)(X)

    X = Dense(classes, activation='softmax', name='fc' + str(classes))(X)

    model = Model(inputs=X_input, outputs=X, name='TestModel')


    return model
