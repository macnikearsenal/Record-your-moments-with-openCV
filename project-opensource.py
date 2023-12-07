<<<<<<< HEAD

import speech_recognition as sr
import threading
import pygame
import pygame.camera
import cv2


# global user_speak
# user_speak = "None"
# num = 1

# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         global user_speak
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source, duration=5)
#             print("Say Something")
#             speech = r.listen(source)
#             try:
#                 audio = r.recognize_google(speech, language="ko-KR")
#                 user_speak = audio
#                 print("Your speech thinks like\n " + audio)
#             except sr.UnknownValueError:
#                 print("Your speech can not understand")
#             except sr.RequestError as e:
#                 print("Request Error!; {0}".format(e))

# def new_video_play(window,video_address):
#     video = cv2.VideoCapture(video_address)
#     success, video_image = video.read()
#     fps = video.get(cv2.CAP_PROP_FPS)
#     clock = pygame.time.Clock()

#     run = success
#     while run:
#         clock.tick(fps)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
        
#         success, video_image = video.read()
#         if success:
#             video_surf = pygame.image.frombuffer(
#                 video_image.tobytes(), video_image.shape[1::-1], "BGR")
#         else:
#             run = False
#         window.blit(video_surf, (0, 0))
#         pygame.display.flip()

#메인 함수 시작
while(1):
    # t = Worker("user_record")                # sub thread 생성
    # t.start() 

    # video = cv2.VideoCapture("assets/1.mp4")
    # success, video_image = video.read()
    # fps = video.get(cv2.CAP_PROP_FPS)

    # window = pygame.display.set_mode(video_image.shape[1::-1])
    # clock = pygame.time.Clock()
    num = 1
    # run = success
    while True:
        #clock.tick(fps)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
             
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("Say Something")
            speech = r.listen(source)
            try:
                audio = r.recognize_google(speech, language="ko-KR")
                user_speak = audio
                print("Your speech thinks like\n " + audio)
                if  "안녕" in user_speak:
                    pygame.camera.init()
                    cameras =pygame.camera.list_cameras()
                    cam = pygame.camera.Camera(cameras[0])
                    cam.start()
                    image = cam.get_image()
                    pygame.image.save(image, 'image/'+str(num)+'.jpg')
                    num = num +1
                    cam.stop()

            except sr.UnknownValueError:
                print("Your speech can not understand")
            except sr.RequestError as e:
                print("Request Error!; {0}".format(e))
            # if  "안녕" in user_speak:
            #     #new_video_play(window,"assets/countdown.mp4")

            #     pygame.camera.init()
            #     cameras =pygame.camera.list_cameras()
            #     cam = pygame.camera.Camera(cameras[0])
            #     cam.start()
            #     image = cam.get_image()
            #     pygame.image.save(image, 'image/'+str(num)+'.jpg')
            #     num = num +1
            #     cam.stop()
                
            # if user_speak is not "None":
            #     user_speak = "None"
                # t = Worker("user_record")                # 이미 종료되었다면 sub thread 생성
                # t.start() 

                
        # success, video_image = video.read()
        # if success:
        #     video_surf = pygame.image.frombuffer(
        #         video_image.tobytes(), video_image.shape[1::-1], "BGR")
        # else:
        #     run = False
        # window.blit(video_surf, (0, 0))
#         pygame.display.flip()

# pygame.quit()


=======
print("hellow word")
>>>>>>> 2db71f7b7cf7c270c76640a7111037b5e86a3039
