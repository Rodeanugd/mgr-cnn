import os
from pydub import AudioSegment

# splitting the audio files into 3 second clips
def splitfiles(genres):
    try:

        i = 0
        for g in genres:
          j=0
          print(f"{g}")
          for filename in os.listdir(os.path.join('../Data Model/genres/',f"{g}")):

            song  =  os.path.join(f'../Data Model/genres/{g}/',f'{filename}')
            j = j+1
            for w in range(0,10):
              i = i+1

              t1 = 3*(w)*1000
              t2 = 3*(w+1)*1000
              newAudio = AudioSegment.from_wav(song)
              new = newAudio[t1:t2]
              new.export(f'./content/audio3sec/{g}/{g+str(j)+str(w)}.wav', format="wav")
    except:
        print("error")
