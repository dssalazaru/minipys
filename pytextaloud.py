from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
lang = 'es'
msg = 'Esto es un audio automatico'
sp = gTTS(text = msg, lang = lang, slow = False)
sp.save(audio)
playsound(audio)