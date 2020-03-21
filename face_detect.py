import cv2, sys, numpy, os
import threading
import time
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils

class RecognizeThread(threading.Thread):
    def __init__(self, interval):

        threading.Thread.__init__(self)     
        self.interval = interval  # seconds between calls
        self.runable = True

    def run(self):
        #global score # make score global for this thread context
        while True:
            im = webcam.read()
            im = imutils.resize(im, width=400)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow('OpenCV', im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            fps.update()

    def stop(self):
        fps.stop()
        self.runable = False

haar_file = 'haarcascade_frontalface_alt2.xml'


print('Training...')

#use LBPHFace recognizer on camera frame
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = WebcamVideoStream(src=0).start()
fps = FPS().start()
#webcam = cv2.VideoCapture(0)


recognize_thread = RecognizeThread(5)
recognize_thread.start()

