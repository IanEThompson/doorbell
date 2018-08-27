import serial
import time
import pygame

pygame.init()
pygame.mixer.init()

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

ser = serial.Serial("/dev/ttyUSB0",9600, timeout=10)
time.sleep(3) #wait for connection to complete

while True:
    dataIn=ser.readline().decode("utf-8")
    if dataIn[:6] == "Button":
        btnPressed = int(dataIn[7:8])
#        print("Button ", btnPressed)
        playAudio(btnPressed)
        

    