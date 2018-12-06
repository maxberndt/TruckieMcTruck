import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) #IN1 Steering
    gpio.setup(22, gpio.OUT) #IN2 Steering
    gpio.setup(23, gpio.OUT) #IN3 RearEngine
    gpio.setup(24, gpio.OUT) #IN4 RearEngine

def rightForward(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(17, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def leftForward(tf):
    init()
    gpio.output(24, False)
    gpio.output(23, True)
    gpio.output(17, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.cleanup()

time.sleep(3)
print "forward"
forward(4)
