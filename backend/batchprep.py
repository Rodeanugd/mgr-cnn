from imports import *


def prepare_batches():
    train_dir = "./content/spectrograms3sec/train/"
    train_datagen = ImageDataGenerator(rescale=1. / 255)
    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(288, 432), color_mode="rgba", class_mode='categorical', batch_size=32 )

    validation_dir = "./content/spectrograms3sec/validation/"
    validation_datagen = ImageDataGenerator(rescale=1. / 255)
    validation_generator = validation_datagen.flow_from_directory(validation_dir, target_size=(288, 432), color_mode='rgba', class_mode='categorical', batch_size=32)

    test_dir = "./content/spectrograms3sec/test/"
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(test_dir, target_size=(288, 432),  color_mode='rgba', class_mode='categorical', batch_size=32)

    full_dir = "./content/spectrograms3sec/test/"
    full_datagen = ImageDataGenerator(rescale=1. / 255)
    full_generator = full_datagen.flow_from_directory(full_dir, target_size=(288, 432), color_mode='rgba',
                                                      class_mode='categorical', batch_size=32, shuffle=False)

    return train_generator, validation_generator, test_generator, full_generator
