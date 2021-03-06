import serial
import time
import pygame
from gpiozero import Button
from signal import pause

#playAudio function includes filenames of mp3 files to play
def playAudio(button):
    #stop any music already playing
    pygame.mixer.music.stop()
    
    #choose which mp3 to play
    if button == btn[0]:
        file = '/home/pi/Music/DrivingInMyCar.mp3'
    elif button == btn[1]:
        file = '/home/pi/Music/BennyHill.mp3'
    elif button == btn[2]:
        file = '/home/pi/Music/SliceOfHeaven.mp3'
    elif button == btn[3]:
        file = '/home/pi/Music/StarWars.mp3'
    elif button == btn[4]:
        file = '/home/pi/Music/WipeOut.mp3'
    else:
        return None
    
    #load and play the mp3 file
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

#initialise pygame mixer
pygame.init()
pygame.mixer.init()

#create button instances from button[0] to button[11]
btn = []
buttonPin = [2,3,4,17,27,22,10,9,11,5,6,13]
for i in range(0,12):
    x = Button(buttonPin[i])
    btn.append(x)

#assign the playAudio event for each button
for i in range(0,12):
    btn[i].when_pressed=playAudio

#everything's set up. Now just wait for a button to be pressed
pause()
