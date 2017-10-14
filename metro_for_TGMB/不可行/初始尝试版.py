from moviepy.editor import *
import cv2
import numpy as np
from itertools import cycle
from threading import Timer
import pygame
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("/Users/Nora/Desktop/metro_for_TGMB/sound.wav")
def xrange(x,y):

    return iter(range(x,y))
timeSignature =4
x=int(input("tempo"))
metSpeed = 60.0 / x
count = cycle(xrange(1, timeSignature + 1))
clip = (VideoFileClip('/Users/Nora/Desktop/metro_for_TGMB/test.mp4')
        .fx( vfx.speedx, x/40.0))
clip.preview()
"""
clip.write_videofile('1.mp4')
cap=cv2.VideoCapture('1.mp4')
frame_counter = 0
def visual():
    countDisplay = next(count)
    #print (countDisplay)
    sounda.play()
    Timer(metSpeed, visual).start()
visual()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow("frame", frame)
    else:
       print('newloop')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(25) & 0xFF == ord('q'):
       break
cap.release()

"""
 
 
 

 
