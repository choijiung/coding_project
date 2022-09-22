import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as sourse:
    print("듣고있어여")
    audio = r.listen(sourse)

try:
    # text = r.recognize_google(audio, language = 'en-US')
    # print(text) 
    text = r.recognize_google(audio, language = 'ko')
    print(text) 
except sr.UnknownValueError:
    print("인식실패")
except sr.RequestError as e:
    print("요청실패: {0}".format(e))

 