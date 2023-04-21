import pyttsx3
import speech_recognition as sr
import os
import webbrowser


engine = pyttsx3.init('espeak') #taking voices form computer 
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3') #setting the female voice
engine.setProperty('rate',160) #speaking speed = 130 (default 200)


def speak(audio):  #defining speak function
    engine.say(audio)
    engine.runAndWait()

def takeCommand():  # it take inputs from microphone and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system('clear')
        print("Speak now, Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please.....")
        return "None"
    return query


if __name__ == "__main__":
    query = takeCommand().lower() #taken command will be converted in lowercase and stored in query
    
    if 'open google' in query:
        speak("opening google...")
        webbrowser.open('google.com')
    elif 'open github' in query:
        speak("opening git hub...")
        webbrowser.open('https://github.com/')
    elif 'open rv college' in query:
        speak("opening rv college website...")
        webbrowser.open('https://rvce.edu.in/')
    elif 'open w3school' in query:
        speak("opening w3school...")
        webbrowser.open('https://www.w3schools.com/')
    elif 'open stack overflow' in query:
        speak("opening stackoverflow...")
        webbrowser.open('https://stackoverflow.com/')
    elif 'open tutorials point' in query:
        speak("opening tutorials point...")
        webbrowser.open('https://www.tutorialspoint.com/index.htm')
    elif 'open geeks for geeks' in query:
        speak("opening geeks for geeks...")
        webbrowser.open('https://www.geeksforgeeks.org/')
    elif 'open hackerrank' in query:
        speak("opening hacker rank...")
        webbrowser.open('https://www.hackerrank.com/')
    else:
        speak("I didnt understand,say that again please")
