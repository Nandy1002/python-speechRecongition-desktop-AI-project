import pyttsx3
import datetime

engine = pyttsx3.init('espeak') #taking voices form computer 
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3') #setting the female voice
engine.setProperty('rate',160) #speaking speed = 130 (default 200)


def speak(audio):  #defining speak function
    engine.say(audio)
    engine.runAndWait()

def wishMe():   #wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hey! I am Iris, Welcome to Desktop AI , Please tell me how may i help you")  #welcome note after greeting


if __name__=="__main__":
    wishMe() 
    