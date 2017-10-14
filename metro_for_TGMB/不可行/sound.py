from itertools import cycle
from threading import Timer
import pygame
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("/Users/Nora/Desktop/metro_for_TGMB/sound.wav")

def xrange(x,y):

    return iter(range(x,y))
#prompts user to enter the beats per minute
x = int(input("BPM:"))

#prompts user to enter the amount of counts per cycle
timeSignature = int(input("How many counts?"))

#calculates the count interval using the user's BPM
metSpeed = 60.0 / x 

#cycles through the defined range
count = cycle(xrange(1, timeSignature + 1))


#prints the counts in the range in order one at a time
def visual():
    countDisplay = next(count)
    #print (countDisplay)
    sounda.play()
    Timer(metSpeed, visual).start()
    
#calls the visual function
visual()
