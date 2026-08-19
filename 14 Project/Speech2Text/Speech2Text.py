
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# code for loading audio file, and converting the speech into text:

# Reading from the audio file of .wav format
'''
def audiofile2Text(audio):
    with sr.AudioFile(audio) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        # it uploads the file to Google and grabs the output
        return text

# specify filename/path
file= "long_speech.wav"

# call audiofile2text()
output= audiofile2Text(file1)
print(output)
'''

# Reading from the Microphone:
# install the library: pip3 install pyaudio
'''
def microphn2text():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Start Speaking")
        audio_data = r.record(source, duration=5)
        # hear from microphone for 5sec and then convert that speech into text
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        return text

# call microphn2text():
output= microphn2text()
print(output)
'''
