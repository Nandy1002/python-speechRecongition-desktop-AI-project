import os

# generate voice using mbrolla voice without pyttsx3
def speak(text):
    print(f"IRIS Said : {text}")
    text = "'"+text+"'"
    os.system(f"espeak -v mb-us1 -s 140 {text}")

# speak("This is a sample text using embrolla voice pack")