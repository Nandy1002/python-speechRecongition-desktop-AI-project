import customtkinter as ctk # gui module 
import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications
import webbrowser as wb  #for controlling the webbrowsers
import wikipedia #wikipedia search 
import customtkinter as ctk #for the gui


#configuring speak engine with pyttsx3


def speak1():
    engine = pyttsx3.init() #initialization
    #engine.setProperty('voice', 'english_rp+f5') #setting the female voice
    #engine.setProperty('rate',180) #speaking speed = 130 (default 200)
    engine.say(entry1.get())
    engine.runAndWait()
    

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
        entry2.placeholder_text=query
        print(f"You said: {query}\n")  # User query will be printed.

    except Exception:
        pass
        # print(e)
        # Say that again will be printed in case of improper voice
        # print("Say that again please...")
        # return "None"  # None string will be returned
    return query

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.geometry("1080x720")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=40,padx=60,fill="both",expand=True)

label = ctk.CTkLabel(master=frame, text="IRIS DESKTOP AI", text_font=("Varela Round",24))
label.pack(pady=12,padx=10)

box = ctk.CTkTextbox(master=frame)
box.pack(pady=10)
entry1 = ctk.CTkEntry(master=frame,placeholder_text="AI Text")
entry1.pack(pady=12,padx=10)
entry2 = ctk.CTkEntry(master=frame,placeholder_text="AI Text")
entry2.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text="Speak", command=takeCommand)
button.pack(pady=12,padx=10)

root.mainloop()

 