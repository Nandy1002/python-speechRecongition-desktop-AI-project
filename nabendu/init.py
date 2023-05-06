import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications
import webbrowser as wb  #for controlling the webbrowsers
import wikipedia #wikipedia search
import customtkinter as ctk
from PIL import Image, ImageTk

#configuring speak engine with pyttsx3

engine = pyttsx3.init() #initialization
engine.setProperty('voice', 'english_rp+f5') #setting the female voice
engine.setProperty('rate',130) #speaking speed = 130 (default 200)
def speak1(text):
    engine.say(text)
    engine.runAndWait()
    aiTextBox.insert(text)

# generate voice using mbrolla voice without pyttsx3

def speak2(text):
    print(f"IRIS Said : {text}")
    text = "'"+text+"'"
    os.system(f"espeak -v mb-us1 -s 150 {text}")


# get audio from microphone


r=sr.Recognizer()
def recognize_speech():
    # Use the microphone as the audio source for speech recognition
    with sr.Microphone() as source:
        # Adjust the recognizer for ambient noise
        r.adjust_for_ambient_noise(source)
        # Listen for speech and convert it to text
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # Display the recognized text in the output label
            output_text.configure(text="You said: " + text)
        except sr.UnknownValueError:
            # Handle unrecognized speech
            output_text.configure(text="Sorry, I didn't catch that.")
        except sr.RequestError as e:
            # Handle network errors
            output_text.configure(text="Sorry, I can't access the Google Speech Recognition service: {0}".format(e))

#user defined functions for IRIS functionalities

#wishme function for wishing on start
def wishMe():   #wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak1("Good Morning!")
    elif hour>=12 and hour<18:
        speak1("Good Afternoon!")
    else:
        speak1("Good Evening!")

#speak1("Hey! I am Iris an Desktop AI , Please tell me, how may I help you?")  


root = ctk.CTk()
root.title("IRIS")
root.geometry("1080x720")
root._set_appearance_mode("dark")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20)

logo = ctk.CTkImage(Image.open(
    "/home/nabendu/Documents/MCA/projects/python-speechRecongition-desktop-AI-project/main/img/walle.png"), size=(200, 180))
label = ctk.CTkLabel(frame, image=logo, text="")
label.grid(row=0, column=0, pady=0, padx=0)

aiTextBox = ctk.CTkTextbox(master=frame, height=100, width=500)
aiTextBox.grid(row=0, column=1, pady=10, padx=50)

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=10)

output_text = ctk.CTkTextbox(master=frame2, height=50, width=500)
output_text.grid(row=0, column=0, padx=30, pady=10)

command = ctk.CTkButton(master=frame2, text="Enter Command",
                        height=50, command=recognize_speech)
command.grid(row=0, column=1, padx=50, pady=10)


root.mainloop()
