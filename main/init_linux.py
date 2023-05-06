import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications
import webbrowser as wb  #for controlling the webbrowsers
import wikipedia #wikipedia search 

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

    except Exception:
        pass
        # print(e)
        # Say that again will be printed in case of improper voice
        # print("Say that again please...")
        # return "None"  # None string will be returned
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

wishMe()
while(True):
    
    query = takeCommand().lower() #taking user queries
    
    #open firefox 
    if 'open firefox' in query:
        speak2("Opening Firefox Browser...")
        wb.open()

    #open chrome
    elif 'open chrome' in query:
        speak2("Opening Chrome Browser...")
        chrome_path = '/usr/bin/google-chrome %s'
        wb.get(chrome_path).open('google.com')

    # libreoffice commands
    elif 'open libra office' in query:
        speak2("Opening Libreoffice")
        os.system("libreoffice")

    elif 'open word document' in query:
        speak2("Opening Empty word document in Libreoffice")
        os.system("lowriter")
    
    elif 'open spreadsheet document' in query:
        speak2("Opening Empty SpreadSheet document in Libreoffice")
        os.system("localc")
    
    elif 'open presentation document' in query:
        speak2("Opening Empty Presentation Document in Libreoffice")
        os.system("loimpress")

    #youtube
    elif 'open youtube' in query:
        speak2("Opening Youtube...")
        wb.open('youtube.com')
    
    #music system
    elif 'play music' in query:
        speak2("Playing music from Rhythmbox")
        os.system("rhythmbox-client --play")
    
    elif 'play next' in query:
        speak2("Playing next music from Rhythmbox")
        os.system("rhythmbox-client --next")

    elif 'play previous' in query:
        speak2("Playing previous music from Rhythmbox")
        os.system("rhythmbox-client --previous")
        os.system("rhythmbox-client --previous")
        
    elif 'pause music' in query:
        speak2("Paused Music from Rhythmbox")
        os.system("rhythmbox-client --pause")
        
    elif 'open rhythm box' in query:
        speak2("Opening Rhythmbox...")
        os.system("rhythmbox-client")

    elif 'wikipedia' in query:
        speak2("Searching in Wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak2("According to Wikipedia , "+results)

    #visual studio code
    elif 'open code' in query:
        speak2("Opening Visual Studio Code Editor")
        os.system("code")
        
    elif 'goodbye' in query:
        speak2("See you next time")
        exit()
    else :
        speak2("Plsease say again.")