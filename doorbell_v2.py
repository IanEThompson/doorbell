import serial
import time
import pygame
from gpiozero import Button
from signal import pause

pygame.init()
pygame.mixer.init()

#create button instance
button1 = Button(2)
button2 = Button(3)
button3 = Button(4)
button4 = Button(17)
button5 = Button(27)
button6 = Button(22)
button7 = Button(10)
button8 = Button(9)
button9 = Button(11)
button10 = Button(5)
button11 = Button(6)
button12 = Button(13)

def playAudio(button):
    pygame.mixer.music.stop()    
    if button == button1:
        file = '/home/pi/Music/DrivingInMyCar.mp3'
    elif button == button2:
        file = '/home/pi/Music/BennyHill.mp3'
    elif button == button3:
        file = '/home/pi/Music/SliceOfHeaven.mp3'
    elif button == button4:
        file = '/home/pi/Music/StarWars.mp3'
    elif button == button5:
        file = '/home/pi/Music/WipeOut.mp3'
    else:
        return None
    
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

button1.when_pressed=playAudio
button2.when_pressed=playAudio
button3.when_pressed=playAudio
button4.when_pressed=playAudio
button5.when_pressed=playAudio
button6.when_pressed=playAudio
button7.when_pressed=playAudio
button8.when_pressed=playAudio
button9.when_pressed=playAudio
button10.when_pressed=playAudio
button11.when_pressed=playAudio
button12.when_pressed=playAudio


pause()
