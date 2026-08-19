import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good day...")

    speak("I am Jarvis sir. Please tell me how may I help you")


def takecommand():
    #It microphone into rom user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
        print('Hello')

    except Exception as e:
       # pass e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    takecommand()
    print("good")
