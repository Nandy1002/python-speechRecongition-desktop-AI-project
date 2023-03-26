#failed

import speech_recognition as sr
import os
import chatbot
from speak2 import speak
from chatterbot import ChatBot
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

speak("Hi I am IRIS.")

query = takeCommand().lower()


chatbot = ChatBot("Chatpot")


exit_conditions = (":q", "quit", "exit")


print(f"🪴 {chatbot.get_response(query)}")