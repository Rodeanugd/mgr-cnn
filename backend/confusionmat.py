from tensorflow.keras.optimizers import  Adam
from imports import *
import cnn
import batchprep
import keras.backend as K
from tensorflow.keras.callbacks import ReduceLROnPlateau
from keras.models import model_from_json
from pydub import AudioSegment
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import librosa
from tensorflow.keras.utils import img_to_array, load_img
import batchprep as bp
import sklearn.metrics as metrics
import seaborn as sn
import pandas as pd


genres = 'blues classical country disco hiphop jazz metal pop reggae rock'
genres = genres.split()

#loading model
def load_model():
    json_file = open('model_v4.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model_v4.h5")
    return model


def get_f1(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
    return f1_val

#main
def stats():
    model = load_model()
    full_generator = bp.prepare_batches()[3]
    predictions = model.predict(full_generator)
    predicted_classes = np.argmax(predictions, axis=1)
    print(predicted_classes)
    true_classes = full_generator.classes
    class_labels = list(full_generator.class_indices.keys())

    report = metrics.classification_report(true_classes, predicted_classes, target_names=class_labels)
    print(report)

    model.compile(optimizer=Adam(learning_rate=0.005), loss='categorical_crossentropy', metrics=['accuracy', get_f1])
    evaluation = model.evaluate(full_generator)
    print(evaluation)




    confusion_matrix = metrics.confusion_matrix(y_true=true_classes, y_pred=predicted_classes, )
    print(confusion_matrix)

    df_cm = pd.DataFrame(confusion_matrix, index=[i for i in genres],
                         columns=[i for i in genres], dtype='int')
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=True, fmt='d')
    plt.savefig(f'./figures/v4/confusion_matrix.png')

    accuracy = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if(i == j):
                accuracy += confusion_matrix[i][j]
    accuracy /= 2000
    print("accuracy: ", accuracy)


stats()



