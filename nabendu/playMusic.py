import pyttsx3
import speech_recognition as sr
import os

#configuring speak engine with pyttsx3
engine = pyttsx3.init() #initialization
engine.setProperty('voice', 'english_rp+f1') #setting the female voice
engine.setProperty('rate',180) #speaking speed = 130 (default 200)

#speak function
def speak(text):
    engine.say(text)
    print("IRIS said: "+text)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system('clear')
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"You said: {query}\n")  #User query will be printed.

    except Exception as e:
    # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

speak("hi, how can i help you today?")

#the user query's stored here
query = takeCommand().lower()

if 'play music' in query:
    speak("Playing music from Rhythmbox")
    os.system("rhythmbox-client --play")
    
elif 'play next' in query:
    speak("Playing next music from Rhythmbox")
    os.system("rhythmbox-client --next")

elif 'play previous' in query:
    speak("Playing previous music from Rhythmbox")
    os.system("rhythmbox-client --previous")
    os.system("rhythmbox-client --previous")
    
elif 'pause music' in query:
    speak("Paused Music from Rhythmbox")
    os.system("rhythmbox-client --pause")
    
elif 'open rhythm box' in query:
    speak("Opening Rhythmbox...")
    os.system("rhythmbox-client")