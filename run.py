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
import google.generativeai as genai




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

    speak("Hii I am your virtual desktop Assistance. How can I help you today!")

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

            if 'wikipedia' in  self.query:
              speak('searching wikipidia...')
              query = self.query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences = 2)
              speak("according to wikipedia")
              speak(results)
              print(results)
              continue


            elif 'ok stop' in self.query:
                speak("thank you ma'am, for using me. Have a good day")
                sys.exit()


            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
                continue

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")
                continue

            elif 'play song on youtube' in self.query:
                pywhatkit.playonyt("Ram siya ram siya ram")
                speak("playing song on youtube")
                continue

            elif 'open wikipedia' in self.query:
                webbrowser.open("www.wikipedia.com")
                speak("opening wikipedia")
                continue

            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")
                speak("opening facebook")
                continue

            elif 'open vs code' in self.query:
             codePath = "C:\\Users\\khush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
             continue

            elif 'open java terminal' in self.query:
                codePath = "D:\\All Programs\\Intellij\\IntelliJ IDEA Community Edition 2021.1\\bin\\idea64.exe"
                os.startfile(codePath)
                speak("opening Intellij")
                continue

            elif 'open whatsapp' in  self.query:
               webbrowser.open("www.whatsapp.com")
               speak("opening whatsapp")
               continue

            elif 'open cmd' in self.query:
                os.system("start cmd")
                speak("opening command prompt")
                continue

            elif 'what is the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f" the time is {strTime}")
                continue

            elif 'thank you' in self.query:
                speak("welcome. Have a good day")
                continue

            elif 'how are you' in self.query:
                speak("i am doing well. thanks for asking. what about you")
                continue

            elif 'i am also fine' in self.query:
                speak("oh that's great")
                continue

            elif 'what is your name' in self.query:
                speak("I don't have name . I am your virtual desktop Assistance")
                continue

            elif 'open stackoverflow' in self.query:
              webbrowser.open("stackoverflow.com")
              continue


            elif 'open chat gpt' in self.query:
                webbrowser.open('www.chat.openai.com')
                speak("opening chat GPT")
                continue

            elif 'open linkedin' in self.query:
                webbrowser.open('www.linkedin.com')
                speak("opening linkedin")
                continue

            elif 'open instagram' in self.query:
             webbrowser.open("www.instagram.com")
             speak("opening instagram")
             continue

            elif 'prime minister of india' in self.query:
                speak("the prime minister of india is Naredra modi")
                continue


            elif 'open notepad' in self.query:
                 notepath = "c:\\Windows\\system32\\notepad.exe"
                 os.startfile(notepath)
                 speak("notepad is opening")
                 continue

            elif 'ip address' in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your ip address is{ip}")
                continue

            elif 'president of india' in self.query:
                speak("the president of india is Droupati Murmu")
                continue

            elif 'cheif minister of maharashtra' in self.query:
                speak("the cheif minister of maharashtra is Eknath Shinde")
                continue


            elif 'nagpur is famous for' in self.query:
                speak("orange city")
                continue

            elif 'king of birds in india' in self.query:
                speak("peacock is the king of birds in india")

            elif 'famous cricketer of india' in self.query:
                speak("Sachin Tendulkar is a retired Indian cricketer widely considered one of the greatest batsmen in the history of the sport")
                continue

            # else:
            #     speak("sorry i did not understand")
                

            genai.configure(api_key="AIzaSyDJaoyaFsI5-3hvjEsohWi4xra9Q87Xk7s")
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(self.query)
            print(response.text)
            speak(response.text)


            speak("Ma'am , you have any other work.Please tell me.")



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
        
        self.label_7 = QMovie("./lib/jarvisAi.gif", QByteArray(), self)
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










