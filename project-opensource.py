import speech_recognition as sr
import pygame
import pygame.camera


num = 1
while True:
    print("준비중 ...")

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
          

