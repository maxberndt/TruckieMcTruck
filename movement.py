import RPi.GPIO as gpio
import sys, termios, tty, os, time
import pygame

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(25, gpio.OUT) #IN1 Steering
    gpio.setup(22, gpio.OUT) #IN2 Steering
    gpio.setup(23, gpio.OUT) #IN3 RearEngine
    gpio.setup(24, gpio.OUT) #IN4 RearEngine
    gpio.setup(4, gpio.OUT) #BLINKER1

    gpio.output(25, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    gpio.output(4, False)

def leftForward(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

def leftBackward(tf):
    init()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

def rightForward(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(25, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def rightBackward(tf):
    init()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(25, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()
