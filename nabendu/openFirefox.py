from speak2 import speak
import speech_recognition as sr
import os
import webbrowser


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

if 'open firefox' in query:
    speak("Opening Firefox Browser...")
    firefox_path = '/usr/bin/firefox %s'
    webbrowser.get(firefox_path).open('google.com')
else:
    speak("I didnt understand, Please Say again")