
import speech_recognition as sr
import threading
import pygame
import pygame.camera
import cv2


global user_speak
user_speak = "None"
num = 1

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        global user_speak
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("Say Something")
            speech = r.listen(source)
            try:
                audio = r.recognize_google(speech, language="ko-KR")
                user_speak = audio
                print("Your speech thinks like\n " + audio)
            except sr.UnknownValueError:
                print("Your speech can not understand")
            except sr.RequestError as e:
                print("Request Error!; {0}".format(e))
