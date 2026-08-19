import speech_recognition as sr
import webbrowser as wb
import os

net_path='C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'

r=sr.Recognizer()
with sr.Microphone() as source:
	print('say somthing!..')
	audio=r.listen(source)
	text=r.recognize_google(audio)
	print(text)
	print('Done')
	
try:
	text=r.recognize_google(audio)
	print('Google thinks you said:\n'+text)
	f_text='https://www.google.co.in/search?q='+text
	wb.get(net_path).open(f_text)
	
except Exception as e:
	print(e)
	