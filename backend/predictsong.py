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

#converting to mp3
def mp3_to_wav(file):
    new_file = AudioSegment.from_mp3(file)
    new_file.export("sample.wav", format="wav")


#creating spectrogram
def create_spectro(wav, n):
    y,sr = librosa.load(wav, duration=3)
    mels = librosa.feature.melspectrogram(y=y, sr=sr)
    fig = plt.Figure()
    canvas = FigureCanvas(fig)
    p = plt.imshow(librosa.power_to_db(mels, ref=np.max))
    plt.savefig('./download/melspectrogram'+n+'.png')


#main
def predict(file):
    model = load_model()
    predictions = []
    wav = AudioSegment.from_wav(file)
    t1=0;
    t2=3;
    print(len(wav))
    while(t2 *1000 <= len(wav)):
        snippet = wav[1000 * t1:1000 * t2]
        snippet.export('./download/'+"snippet" +str(t2 // 3) + ".wav", format='wav')
        create_spectro('./download/'+"snippet" +str(t2 // 3) + ".wav", str(t2 // 3))
        image_base = load_img('./download/melspectrogram'+str(t2 // 3) +'.png', color_mode='rgba', target_size=(288,432))
        prediction = predict_one(image_base, model)
        predictions.append(prediction)
        t1 += 3
        t2 += 3

    prediction_mean = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (0, 10):
        for prediction in predictions:
            prediction_mean[i] += prediction[i] / (t2 // 3)

    for i in range (0, 10):
        print(genres[i] + ": " + str(prediction_mean[i]))
    print(genres[np.argmax(prediction_mean)])
    return(genres[np.argmax(prediction_mean)])





#predicting song
def predict_one(image_base, model):
    image = img_to_array(image_base)
    image = np.reshape(image, (1, 288, 432, 4))
    prediction = model.predict(image/255)
    prediction = prediction.reshape((10,))
    return prediction


# predict('./download\\sample.wav')
