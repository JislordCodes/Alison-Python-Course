import speech_recognition as sr
import pyaudio
from selenium import webdriver

class voice:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()
    def listenOnMic(self):
        while True:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio).lower()

            print(command)

listerner = voice()
