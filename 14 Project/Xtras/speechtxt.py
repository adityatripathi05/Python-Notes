import speech_recognition as sr
from gtts import gTTS
import pyaudio 
import os 
r=sr.Recognizer()
with sr.Microphone()as source:
	print('what you went to know ')
	r.pause_threshold=1
	r.adjust_for_ambient_noise(source,duration=1)
	audio = r.listen(source)
	try:
		text=r.recognize_google(audio).lower()
		print('Your question:'+text+'\n')
	except:
		exit(0)