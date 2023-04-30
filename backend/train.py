import os

# from keras.callbacks import ReduceLROnPlateau

os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.6/bin")
os.add_dll_directory("C:/Misc/CUDNN/zlib/dll_x64")
os.add_dll_directory("C:/Misc/CUDNN/cudnn-windows-x86_64-8.4.0.27_cuda11.6-archive/bin")
os.add_dll_directory("C:/Program Files/NVIDIA/CUDNN/v8.4/bin")
from tensorflow.keras.optimizers import  Adam
from imports import *
import cnn
import batchprep
import keras.backend as K
from tensorflow.keras.callbacks import ReduceLROnPlateau
import matplotlib.pyplot as plt
import json

def get_f1(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
    return f1_val

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

train_generator, validation_generator, test_generator, full_generator = batchprep.prepare_batches()
model = cnn.TestModel(input_shape=(288, 432, 4), classes=10)
opt = Adam(learning_rate=0.005)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy', get_f1])  # try other loss function


reduceLR = ReduceLROnPlateau(monitor="val_loss", factor=0.4, patience=3, min_delta=0.005)  # min_lr?

# model.fit_generator(train_generator, epochs=70, validation_data=validation_generator, callbacks=[reduceLR])  # use normal fit& evaluate
# evaluation = model.evaluate_generator(test_generator)

history = model.fit(train_generator, epochs=70, validation_data=validation_generator, callbacks=[reduceLR])
evaluation = model.evaluate(test_generator)




print("\nEvaluation: ", evaluation)

model_json = model.to_json()
with open("model_n17.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model_n17.h5")

# plot and save accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('./figures/n117/acc.png')
plt.clf()

# plot and save loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('./figures/n117/val.png')
plt.clf()

# plot and save fitness
plt.plot(history.history['get_f1'])
plt.plot(history.history['val_get_f1'])
plt.title('model fitness')
plt.ylabel('fitness')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('./figures/n117/fit.png')
plt.clf()

# plot and save learning rate
plt.plot(history.history['lr'])
plt.title('model learning rate')
plt.ylabel('learning rate')
plt.xlabel('epoch')
plt.savefig('./figures/n117/lr.png')
plt.clf()

# plot and save train accuracy
plt.plot(history.history['accuracy'])
plt.title('model training accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.savefig('./figures/n117/acc_t.png')
plt.clf()

# plot and save train loss
plt.plot(history.history['loss'])
plt.title('model training loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.savefig('./figures/n117/val_t.png')
plt.clf()

# plot and save training fitness
plt.plot(history.history['val_get_f1'])
plt.title('model validation fitness')
plt.ylabel('fitness')
plt.xlabel('epoch')
plt.savefig('./figures/n117/fit_t.png')
plt.clf()

# plot and save validation accuracy
plt.plot(history.history['val_accuracy'])
plt.title('model validation accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.savefig('./figures/n117/acc_v.png')
plt.clf()

# plot and save validation loss
plt.plot(history.history['val_loss'])
plt.title('model validation loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.savefig('./figures/n117/val_v.png')
plt.clf()

# plot and save validation fitness
plt.plot(history.history['val_get_f1'])
plt.title('model validation fitness')
plt.ylabel('fitness')
plt.xlabel('epoch')
plt.savefig('./figures/n117/fit_v.png')
plt.clf()
