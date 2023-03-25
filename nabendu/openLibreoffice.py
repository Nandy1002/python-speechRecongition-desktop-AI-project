from speak2 import speak
import speech_recognition as sr
import os


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

if 'open libra office' in query:
    speak("Opening Libreoffice")
    os.system("libreoffice")
elif 'open word document' in query:
    speak("Opening Empty word document in Libreoffice")
    os.system("lowriter")
elif 'open spreadsheet document' in query:
    speak("Opening Empty SpreadSheet document in Libreoffice")
    os.system("localc")
elif 'open presentation document' in query:
    speak("Opening Empty Presentation Document in Libreoffice")
    os.system("loimpress")