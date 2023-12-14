
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

def new_video_play(window,video_address):
    video = cv2.VideoCapture(video_address)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()
