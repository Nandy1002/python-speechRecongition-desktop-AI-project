import pyttsx3
# import speech_recognition
# import tkinter as Tk

#configuring speak engine with pyttsx3
engine = pyttsx3.init() #initialization
engine.setProperty('voice', 'english_rp+f5') #setting the female voice
engine.setProperty('rate',130) #speaking speed = 130 (default 200)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# speak("Hello this is a sample voice from espeak")
# for voice in engine.getProperty('voices'):
#     print(voice)

