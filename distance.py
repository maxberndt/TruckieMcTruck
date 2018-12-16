import RPi.GPIO as gpio
import sys, termios, tty, os, time
import pygame

def getDistance():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    GPIO_TRIGGER = 27
    GPIO_ECHO = 17

    gpio.setup(GPIO_TRIGGER, gpio.OUT)
    gpio.setup(GPIO_ECHO, gpio.IN)

        # set Trigger High
    gpio.output(GPIO_TRIGGER, True)

    # set Trigger after 0.1ms low
    time.sleep(0.00001)
    gpio.output(GPIO_TRIGGER, False)

    startTime = time.time()
    endTime = time.time()

    # store start time
    while gpio.input(GPIO_ECHO) == 0:
        startTime = time.time()

    # store arrival
    while gpio.input(GPIO_ECHO) == 1:
        endTime = time.time()

    # elapsed time
    TimeElapsed = endTime - startTime
    # multiply with speed of sound (34300 cm/s)
    # and division by two
    distance = (TimeElapsed * 34300) / 2
    return distance
