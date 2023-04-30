import os

def makedirs(genres):

    try:

        os.makedirs('./content/spectrograms3sec')
        os.makedirs('./content/spectrograms3sec/train')
        os.makedirs('./content/spectrograms3sec/test')
        os.makedirs('./content/spectrograms3sec/validation')


        for g in genres:
            path_audio = os.path.join('./content/audio3sec',f'{g}')
            os.makedirs(path_audio)
            path_train = os.path.join('./content/spectrograms3sec/train',f'{g}')
            path_test = os.path.join('./content/spectrograms3sec/test',f'{g}')
            path_validation = os.path.join('./content/spectrograms3sec/validation',f'{g}')
            os.makedirs(path_train)
            os.makedirs(path_test)
            os.makedirs(path_validation)


    except:
        print("error making directories")
