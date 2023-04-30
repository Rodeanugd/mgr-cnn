import tensorflow as tf
import numpy as np
import scipy
from scipy import misc
import glob
from PIL import Image
import os
import matplotlib.pyplot as plt
import librosa
from keras import layers
from keras.layers import (Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten,
                          Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D)
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.utils import layer_utils
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils.vis_utils import plot_model
from tensorflow.keras.optimizers import Adam
from keras.initializers import glorot_uniform
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pydub import AudioSegment
import shutil
from keras.preprocessing.image import ImageDataGenerator
import random



def generate_spectograms(genres):
    for g in genres:
        j = 0
        print(g)

        for filename in os.listdir(os.path.join('./content/audio3sec',f"{g}")):
            song = os.path.join(f'./content/audio3sec/{g}',f'{filename}')
            j = j+1

            y,sr = librosa.load(song,duration=3)
            mels = librosa.feature.melspectrogram(y=y,sr=sr)
            fig = plt.Figure()
            canvas = FigureCanvas(fig)
            p = plt.imshow(librosa.power_to_db(mels,ref=np.max))
            plt.savefig(f'./content/spectrograms3sec/train/{g}/{g+str(j)}.png')
