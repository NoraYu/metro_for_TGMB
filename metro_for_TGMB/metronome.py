from moviepy.editor import *
import pygame
import sys
import _thread
tempo=float(input("tempo"))
def videoplay(tempo):  
   clip = (VideoFileClip('/Users/Nora/code/metro_for_TGMB/test.mp4')
        .fx( vfx.speedx, tempo/40.0))
   clip.preview() 
def input_thread(list):
    input()
    list.append(None)

def do_stuff():
    list = []
    _thread.start_new_thread(input_thread, (list,))
    while not list:
        videoplay(tempo)
  
do_stuff()
sys.exit()

 
