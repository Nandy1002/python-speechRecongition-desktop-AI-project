from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications
import webbrowser as wb  #for controlling the webbrowsers
import wikipedia #wikipedia search 


def speak():
    #usertext.configure(text="hello world")
    usertext.insert(0, "hello world")
    # engine = pyttsx3.init()
    # engine.say("hello world")
    # engine.runAndWait()
    
    
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
        usertext.insert(0, str(query))
    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


a = takeCommand()
print(a)
root = ttk.Window(themename="solar")
root.geometry("1080x720")
root.title("IRIS DESKTOP AI")

frame1 = ttk.Frame(master=root,height=100,width=900,bootstyle="secondary")
frame1.pack(padx=40,pady=40)

#header = ttk.Label(master=frame1,text="IRIS DESKTOP AI",bootstyle="info")
#header.pack(padx=10,pady=10)
button = ttk.Button(master=frame1,bootstyle="success",text="Take Command")
button.grid(row=0,column=0,padx=10,pady=10)

usertext = ttk.Entry(master=frame1,bootstyle="success")
usertext.grid(row=0,column=1,padx=10,pady=10)

aitext = ttk.Entry(master=frame1,bootstyle="success")
aitext.grid(row=0,column=2,padx=10,pady=10)

root.mainloop()

   