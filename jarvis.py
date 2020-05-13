import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("Hello Sir! I am Jarvis. Please tell me how may I help you?")
        

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        print(e)
        print("Please say again...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir="D:\\songs\\old & ne songs\\old & new song"
            songs=os.listdir(music_dir)
            print(songs)
            value=random.randint(1,50)
            os.startfile(os.path.join(music_dir,songs[value]))
        elif 'the time' in query:
            timeval=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is:{timeval}")

        elif 'open visual studio' in query:
            path="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'quit' in query:
            exit()