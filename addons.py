import RPi.GPIO as gpio
import sys, termios, tty, os, time
import pygame

def blink_left():
    movement.init()
    gpio.output(4, True)
    time.sleep(2)
    gpio.output(4, False)
    gpio.cleanup()

def playsound(file_n):
    pygame.mixer.init()
    pygame.mixer.music.load(file_n)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
