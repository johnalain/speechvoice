#https://youtu.be/NL9M71TnFSc
from  playsound import playsound
import speech_recognition as sr

from gtts import gTTS
# tts = gTTS('hello', lang='ar')
# tts.save('hello.mp3')


r = sr.Recognizer()
with sr.Microphone() as src:
    print('say something......')
    audio = r.listen(src)
try:
    t= r.recognize_google(audio,language='ar-AR')
    print(t)
    f = open('text.txt','a',encoding='UTF-8')
    f.writelines(t +'\n')
    f.close()
    obj=gTTS(text=t,lang='ar',slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')
except sr. UnknownValueError as U:
    print(U)
except sr.RequestError as R:
    print(R)

