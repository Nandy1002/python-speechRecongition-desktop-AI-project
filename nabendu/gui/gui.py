from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image,ImageTk
import pyttsx3 # voice module for  speaking
import speech_recognition as sr # for speech recognition
import datetime # for getting date and time
import os #os module for controling operation system applications
#import sys
import pywhatkit as kt #for google Searches
import webbrowser as wb  #for controlling the webbrowsers
import wikipedia #wikipedia search 

engine = pyttsx3.init()
engine.setProperty('voice', 'english_rp+f5') #setting the female voice
engine.setProperty('rate',130) #speaking speed = 130 (default 200)

def speak1(text):
    #usertext.configure(text="hello world")
    aitext.delete(0,ttk.END)
    aitext.insert(0,text)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def wishMe():   #wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

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
        usertext.delete(0,ttk.END)
        usertext.insert(0, str(query))
    except Exception as e:
        print(e)
        query = usertext.get()
        
    
    query = str(query).lower()
     #open firefox 
    if 'open firefox' in query:
        speak1("Opening Firefox Browser...")
        wb.open('rvce.edu.in')

    #open chrome
    elif 'open chrome' in query:
        speak1("Opening Chrome Browser...")
        chrome_path = '/usr/bin/google-chrome %s'
        wb.get(chrome_path).open('google.com')

    # libreoffice commands
    elif 'open libra office' in query:
        speak1("Opening Libreoffice")
        os.system("libreoffice &")

    elif 'open word document' in query:
        speak1("Opening Empty word document in Libreoffice")
        os.system("lowriter &")
    
    elif 'open spreadsheet document' in query:
        speak1("Opening Empty SpreadSheet document in Libreoffice")
        os.system("localc &")
    
    elif 'open presentation document' in query:
        speak1("Opening Empty Presentation Document in Libreoffice")
        os.system("loimpress &")

    #youtube
    elif 'open youtube' in query:
        speak1("Opening Youtube...")
        wb.open('youtube.com')
    
    #music system
    elif 'play music' in query:
        speak1("Playing music from Rhythmbox")
        os.system("rhythmbox-client --play")
    
    elif 'play next' in query:
        speak1("Playing next music from Rhythmbox")
        os.system("rhythmbox-client --next")

    elif 'play previous' in query:
        speak1("Playing previous music from Rhythmbox")
        os.system("rhythmbox-client --previous")
        os.system("rhythmbox-client --previous")
        
    elif 'pause music' in query:
        speak1("Paused Music from Rhythmbox")
        os.system("rhythmbox-client --pause")
        
    elif 'open rhythm box' in query:
        speak1("Opening Rhythmbox...")
        os.system("rhythmbox-client")

    elif 'wikipedia' in query:
        speak1("Searching in Wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        bodyText.insert(ttk.END,results)
        speak1("According to Wikipedia , "+results)
        aitext.delete(0,ttk.END)
        aitext.insert(0,"According to Wikipedia...")
    #visual studio code
    elif 'open code' in query:
        speak1("Opening Visual Studio Code Editor")
        os.system("code &")
        
    elif 'goodbye' in query:
        speak1("See you next time")
        exit()

    elif 'introduce yourself' in query:
        speak1("Hello, User")
        intro="I am IRIS, An Desktop AI. I can help you in doing your tasks inside your computer and increse your productivity, like -  I can open programs for you or play music or do any google search"
        bodyText.delete(ttk.END)
        bodyText.insert(ttk.END,intro)
        speak(intro)
    elif "search" in query:
        query = query.replace("search","")
        speak1("searching in google...")
        kt.search(query)
    elif "youtube video" in query:
        query = query.replace("youtube video","")
        speak1("Searching in Youtube...")
        kt.playonyt(query)
    elif "open whatsapp" in query:
        speak1("Opening Whatsapp...")
        os.system("whatsapp-for-linux &")
    else :
        speak1("Plsease say again.")
    
    #bodyText.insert(0,sys.stdout)
    #bodyText.insert(ttk.END,sys.stderr)
    


root = ttk.Window(themename="morph")
root.geometry("1080x600")
root.title("IRIS DESKTOP AI")

frame1 = ttk.Frame(master=root,bootstyle=PRIMARY)
frame1.pack(padx=40,pady=40)

ttk.Separator(bootstyle=INFO).pack(fill='x',padx=50)

frame2 = ttk.Frame(master=root,bootstyle="primary")
frame2.pack(padx=40,pady=40)

ttk.Separator(bootstyle=INFO).pack(fill='x',padx=50)

userLabel = ttk.LabelFrame(master=root,text="User Commands",bootstyle=INFO)
userLabel.pack(pady=(40,10))

frame3= ttk.Frame(master=userLabel,bootstyle="primary")
frame3.pack(padx=10,pady=10)


#frame1
img = Image.open("/home/nabendu/Documents/MCA/projects/python-speechRecongition-desktop-AI-project/nabendu/gui/walle.png")

aiImage = ImageTk.PhotoImage(img.resize((100,100)))
aiLabel = ttk.Label(master=frame1,image=aiImage,width=50)
aiLabel.grid(row=0,rowspan=2,column=0,padx=10,pady=(10,10))


aiTextFrame = ttk.LabelFrame(master=frame1,text=" IRIS AI Says : ",bootstyle=INFO)
aiTextFrame.grid(row=0,column=1,rowspan=2,padx=10)

aitext = ttk.Entry(aiTextFrame,bootstyle="success",width=70)
aitext.insert(0,"Hi! How can I help you today?")
aitext.pack(padx=10,pady=10)

#frame2

bodyFrame = ttk.LabelFrame(master=frame2,text="Body Text",bootstyle=INFO)
bodyFrame.pack()
bodyText = ttk.Text(bodyFrame,height=5,width=100,foreground="blue")
bodyText.pack(padx=20,pady=20)


# frame3


usertext = ttk.Entry(master=frame3,bootstyle="success",width=85)
usertext.insert(0,"Your Spoken Commands here!")
usertext.grid(row=0,column=0,padx=10,pady=10)

button = ttk.Button(master=frame3,bootstyle=(DANGER,OUTLINE),text="Take Command",command=takeCommand)
button.grid(row=0,column=1,padx=10,pady=10)


wishMe()
root.mainloop()

   