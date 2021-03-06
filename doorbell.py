#!/usr/bin/env python3

import serial
import time
import pygame
from gpiozero import Button
from signal import pause

#global variable to count the instances of the playAudio function running
playAudioCount = 0

#playAudio function - called whenever a button is pressed
#The button that is pressed will pass itself as the input parameter
def playAudio(button):
    global playAudioCount
    playAudioCount = playAudioCount + 1

    #stop any music already playing
    pygame.mixer.music.stop()
    
    #choose which mp3 to play
    if button == btn[0]:
        file = '/home/pi/Music/ImperialMarch.mp3'
        volume = 0.8
    elif button == btn[1]:
        file = '/home/pi/Music/PeriodicTableSong.mp3'
        volume = 0.8
    elif button == btn[2]:
        file = '/home/pi/Music/SoLongAndThanksForAllTheFish.mp3'
        volume = 0.8
    elif button == btn[3]:
        file = '/home/pi/Music/DoctorWho.mp3'
        volume = 0.8
    elif button == btn[4]:
        file = '/home/pi/Music/WipeOut.mp3'
        volume = 0.8
    elif button == btn[5]:
        file = '/home/pi/Music/BabyShark.mp3'
        volume = 0.7
    elif button == btn[6]:
        file = '/home/pi/Music/CottonEyeJoe_loud.mp3'
        volume = 0.6
    elif button == btn[7]:
        file = '/home/pi/Music/YaketySax.mp3'
        volume = 0.9
    elif button == btn[8]:
        file = '/home/pi/Music/ThePushbikeSong_loud.mp3'
        volume = 1.0
    elif button == btn[9]:
        file = '/home/pi/Music/SummerOf69_loud.mp3'
        volume = 0.8
    else:
        playAudioCount = playAudioCount - 1
        return None
    
    #load and play the mp3 file
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    #after 15 seconds (if no more buttons have been pressed), stop the music
    time.sleep(15)
    playAudioCount = playAudioCount - 1
    
    print("playAudioCount=",playAudioCount);
    
    if playAudioCount == 0:
        pygame.mixer.music.fadeout(2000)   #fadeout over 2 seconds

#=======================================================
#  Main program starts here
#=======================================================

#initialise pygame mixer
pygame.init()
pygame.mixer.init()

#create 12 button instances from button[0] to button[11]
btn = []    #create empty list for the button instances
buttonPin = [2,3,4,17,27,22,13,6,5,11,9,10]  #list of GPIO pins that buttons are connected to
for i in range(0,12):
    x = Button(buttonPin[i])        #create a new button instance on the appropriate pin
    btn.append(x)                   #add it to the list of button instances
    btn[i].when_pressed=playAudio   #link the new button to the playAudio function

#counter to keep track of how many instances of the playAudio function are running
playAudioCount=0

#everything's set up now; the playAudio function will run whenever a button is pressed
input("Press ENTER to quit")

