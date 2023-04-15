import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications

#configuring speak engine with pyttsx3

engine = pyttsx3.init() #initialization
engine.setProperty('voice', 'english_rp+f5') #setting the female voice
engine.setProperty('rate',130) #speaking speed = 130 (default 200)
def speak1(text):
    engine.say(text)
    engine.runAndWait()

# generate voice using mbrolla voice without pyttsx3

def speak2(text):
    print(f"IRIS Said : {text}")
    text = "'"+text+"'"
    os.system(f"espeak -v mb-us1 -s 150 {text}")


# get audio from microphone

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system('clear')
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

#user defined functions for IRIS functionalities

#wishme function for wishing on start
def wishMe():   #wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak2("Good Morning!")
    elif hour>=12 and hour<18:
        speak2("Good Afternoon!")
    else:
        speak2("Good Evening!")

    speak2("Hey! I am Iris an Desktop AI , Please tell me, how may I help you?")  #welcome note after greeting



#main loop of the program

if __name__=="__main__":
    wishMe()