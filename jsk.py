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



flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("I am JSK Assistant. Please tell me how may I help you")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JSK()
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print("user said:",text)
        except Exception:
            speak("")
            return "None"
        text = text.lower()
        return text

    def JSK(self):
        wish()
        while True:
            self.query = self.STT()
            if 'ok stop' in self.query:
                speak("thank you for using me. Have a good day")
                sys.exit()

            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")

            elif 'play song on youtube' in self.query:
                pywhatkit.playonyt("one touch and i ignite")

            elif 'open wikipedia' in self.query:
                webbrowser.open("www.wikipedia.com")
                speak("opening wikipedia")

            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")
                speak("opening facebook")

            elif 'open vs code' in self.query:
                codePath = "D:\\All Programs\\VS Code\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("opening vs code")

            elif 'open java terminal' in self.query:
                codePath = "D:\\All Programs\\Intellij\\IntelliJ IDEA Community Edition 2021.1\\bin\\idea64.exe"
                os.startfile(codePath)
                speak("opening Intellij")

            elif 'open android studio' in self.query:
                codePath = "D:\\All Programs\\Android Studio\\bin\\studio64.exe"
                os.startfile(codePath)
                speak("opening android studio")

            elif 'open whatsapp' in self.query:
                codePath = "C:\\Users\\Snehal\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(codePath)
                speak("Whatsapp is opening")

            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="D:\music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))

            elif 'open cmd' in self.query:
                os.system("start cmd")
                speak("opening command prompt")

            elif 'what is the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f" the time is {strTime}")

            elif 'thank you' in self.query:
                speak("welcome. Have a good day")

            elif 'how are you' in self.query:
                speak("i am doing well. thanks for asking. what about you")

            elif 'i am also fine' in self.query:
                speak("oh that's great")

            elif 'what is your name' in self.query:
                speak("it just JSK. only JSK")

            elif 'open chat gpt' in self.query:
                webbrowser.open('www.chat.openai.com')
                speak("opening chat GPT")

            elif 'open linkedin' in self.query:
                webbrowser.open('www.linkedin.com')
                speak("opening linkedin")

            elif 'prime minister of india' in self.query:
                speak("the prime minister of india is Naredra modi")

            elif 'open notepad' in self.query:
                codePath = "c:\\Windows\\system32\\notepad.exe"
                os.startfile(codePath)
                speak("notepad is opening")

            elif 'ip address' in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your ip address is{ip}")

            elif 'president of india' in self.query:
                speak("the president of india is Droupati Murmu")

            elif 'cheif minister of maharashtra' in self.query:
                speak("the cheif minister of maharashtra is Eknath Shinde")

            elif 'cheif minister of maharashtra' in self.query:
                speak("the cheif minister of maharashtra is Eknath Shinde")

            elif 'nagpur is famous for' in self.query:
                speak("orange city")

            elif 'king of birds in india' in self.query:
                speak("peacock is the king of birds in india")

            elif 'famous cricketer of india' in self.query:
                speak("Sachin Tendulkar is a retired Indian cricketer widely considered one of the greatest batsmen in the history of the sport")

            else:
                print("sorry i did not understand")


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
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
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())






















# FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

# class Main(QMainWindow,FROM_MAIN):
#     def __init__(self,parent=None):
#         super(Main,self).__init__(parent)
#         self.setupUi(self)
#         self.setFixedSize(1920,1080)
#         self.label_7 = QLabel(self)
#         self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
#         "border:none;")
#         self.exitB.clicked.connect(self.close)
#         self.setWindowFlags(flags)
#         Dspeak = mainT()
#         gif_width = 1000
#         gif_height = 900
#         self.label_7 = QLabel(self)
#         self.label_7.setFixedSize(gif_width, gif_height)
#         horizontal_offset = 350  # Adjust this value as needed
#         self.label_7.move((self.width() - gif_width) // 2 + horizontal_offset, (self.height() - gif_height) // 2)
#         self.movie = QMovie("./lib/jarvisAi.gif")
#         self.label_7.setMovie(self.movie)
#         self.movie.start()
#         self.ts = time.strftime("%A, %d %B")
#         Dspeak.start()
#         self.label.setPixmap(QPixmap("./lib/tuse.png"))
#         self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
#         self.label_5.setFont(QFont(QFont('Acens',8)))
# app = QtWidgets.QApplication(sys.argv)
# main = Main()
# main.show()
# exit(app.exec_())