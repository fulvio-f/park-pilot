#!/usr/bin/env python3

import serial
import pygame

arduinoSerialData = serial.Serial("/dev/ttyACM0", 9600)

pygame.init()
win_width, win_height = 640, 640
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Park Pilot")

bg1, bg2 = pygame.image.load("parking.jpg"), pygame.image.load("waiting.jpg")
car = pygame.image.load("car.png")

x, y, width, height = 70, 320, 200, 200
run, waiting = True, False

beep = last_beep = None

def redraw():
    """ Draws car in each position or draws waiting background"""

    if waiting == False:
        win.blit(bg1, (0,0))
        win.blit(car, (x,y))
    else:
        win.blit(bg2, (0,0))

    pygame.display.update()

while run:

    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if arduinoSerialData.inWaiting() > 0:
        distance = arduinoSerialData.readline().decode('UTF-8')
        distance = distance.replace('\r', '')
        distance = distance.replace('\n', '')
        if distance == '':
            distance = 0
        distance = round(int(distance),-1)
        if 0 <= distance <= 1000 and abs(y-(-0.8*distance+280)) > 20:
            y = int(-0.8*distance + 280)
            waiting = False
        if distance > 1000 or distance < 0:
            waiting = True

    if distance >= 750 and distance < 1000:
        last_beep = beep
        beep = "beep1.wav"
    if distance >= 500 and distance < 750:
        last_beep = beep
        beep = "beep2.wav"
    if distance >= 250 and distance < 500:
        last_beep = beep
        beep = "beep3.wav"
    if distance > 0 and distance < 250:
        last_beep = beep
        beep = "beep4.wav"
    if beep != last_beep:
        music = pygame.mixer.music.load(beep)
        pygame.mixer.music.play(-1)

    redraw()

pygame.quit()
