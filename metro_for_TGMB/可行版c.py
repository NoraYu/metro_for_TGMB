from moviepy.editor import *
import pygame
import sys
tempo=float(input("tempo"))
def videoplay(tempo):  
   clip = (VideoFileClip('/Users/Nora/code/metro_for_TGMB/test.mp4')
        .fx( vfx.speedx, tempo/40.0))
   clip.preview()   
def loopnquit():
  try:
     while True:
       for i in range(0,100000000):
          videoplay(tempo)
  except KeyboardInterrupt:
     pass
loopnquit()
sys.exit()

 
