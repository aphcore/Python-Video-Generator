import os
import time

from pyt2s.services import stream_elements

# en_US_Wavenet_D - male
# en_US_Standard_C - female
fileDir = os.path.dirname(os.path.abspath(__file__))
def getTTS(text1,text2):
    data = stream_elements.requestTTS(f'{text1} . . . . . . . {text2}', stream_elements.Voice.en_US_Standard_C.value)
    with open(os.path.join(fileDir, "./tts.mp3"), '+wb') as file:
        file.write(data)
    time.sleep(2)
    return
