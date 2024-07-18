import pywhatkit
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import wikipedia
from requests import get
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

    class mainT(QThread):
        def __init__(self):
            super(mainT, self).__init__()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open Whatsapp' in query:
            codePath = "C:\\Users\\Snehal\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
            speak("Whatsapp is opeaning")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

    FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


    class Main(QMainWindow, FROM_MAIN):
        def __init__(self, parent=None):
            super(Main, self).__init__(parent)
            self.setupUi(self)
            self.setFixedSize(1920, 1080)
            self.label_7 = QLabel
            self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                     "border:none;")
            self.exitB.clicked.connect(self.close)
            self.setWindowFlags(flags)
            Dspeak = mainT()
            self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
            self.label_7.setCacheMode(QMovie.CacheAll)
            self.label_4.setMovie(self.label_7)
            self.label_7.start()

            self.ts = time.strftime("%A, %d %B")

            Dspeak.start()
            self.label.setPixmap(QPixmap("./lib/tuse.png"))
            self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
            self.label_5.setFont(QFont(QFont('Acens', 8)))


    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    exit(app.exec_())

