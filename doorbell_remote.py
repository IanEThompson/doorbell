import serial
import time
import pygame
from gpiozero import Button

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
    print("Button ", button)  
    if button == 1:
        file = '/home/pi/Music/DrivingInMyCar.mp3'
    elif button == 2:
        file = '/home/pi/Music/BennyHill.mp3'
    elif button == 3:
        file = '/home/pi/Music/SliceOfHeaven.mp3'
    elif button == 4:
        file = '/home/pi/Music/StarWars.mp3'
    elif button == 5:
        file = '/home/pi/Music/WipeOut.mp3'
    else:
        return None
    
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

while True:
    if button1.is_pressed:
        playAudio(1)
    if button2.is_pressed:
        playAudio(2)
    if button3.is_pressed:
        playAudio(3)
    if button4.is_pressed:
        playAudio(4)
    if button5.is_pressed:
        playAudio(5)
    if button6.is_pressed:
        playAudio(6)
    if button7.is_pressed:
        playAudio(7)
    if button8.is_pressed:
        playAudio(8)
    if button9.is_pressed:
        playAudio(9)
    if button10.is_pressed:
        playAudio(10)
    if button11.is_pressed:
        playAudio(11)
    if button12.is_pressed:
        playAudio(12)
    time.sleep(0.1)
    
