#!/usr/bin/env python3

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
        return None
    
    #load and play the mp3 file
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    
#initialise pygame mixer
pygame.init()
pygame.mixer.init()

#create button instances from button[0] to button[11]
btn = []
#buttonPin = [2,3,4,17,27,22,10,9,11,5,6,13]
buttonPin = [2,3,4,17,27,22,13,6,5,11,9,10]
for i in range(0,12):
    x = Button(buttonPin[i])
    btn.append(x)

#assign the playAudio event for each button
for i in range(0,12):
    btn[i].when_pressed=playAudio

#everything's set up. Now just wait for a button to be pressed
#pause()
input("Press ENTER to quit")
