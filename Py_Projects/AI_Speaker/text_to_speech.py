from gtts import gTTS
from playsound import playsound

location = '/Users/Jiung/coding/Py_Projects/AI_Speaker/files'
file_name = location + '/sample.mp3'

#영어 문장
# text = 'pneumonoultramicroscopicsilicovolcanoconiosis'
# tts_en = gTTS(text = text, lang='en')
# tts_en.save(file_name)
# playsound(filename)

#한글 문장
# text = '난방방법변경방밥 '
# tts_en = gTTS(text = text, lang='ko')
# tts_en.save(file_name)
# playsound(file_name)

#긴 문장
with open(location + '/sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tts_en = gTTS(text = text, lang='ko')
tts_en.save(file_name)
playsound(file_name)