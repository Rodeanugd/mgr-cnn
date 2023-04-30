from imports import *

def splitdata(genres):
    directory_train = "./content/spectrograms3sec/train/"
    directory_test = "./content/spectrograms3sec/test/"
    directory_validation = "./content/spectrograms3sec/validation/"

    for g in genres:
        old_test = os.listdir(os.path.join(directory_test, f"{g}"))
        old_validation = os.listdir(os.path.join(directory_validation, f"{g}"))

        for f in old_test:
            shutil.move(directory_test + f"{g}" + "/" + f, "./content/spectrograms3sec/train/" + f"{g}")
        for f in old_validation:
            shutil.move(directory_validation + f"{g}" + "/" + f, "./content/spectrograms3sec/train/" + f"{g}")

        filenames = os.listdir(os.path.join(directory_train, f"{g}"))
        random.shuffle(filenames)
        test_files = filenames[0:200]
        validation_files = filenames[200:400]

        for f in test_files:
            shutil.move(directory_train + f"{g}" + "/" + f, "./content/spectrograms3sec/test/" + f"{g}")
        for f in validation_files:
            shutil.move(directory_train + f"{g}" + "/" + f, "./content/spectrograms3sec/validation/" + f"{g}")
