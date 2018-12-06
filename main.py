import RPi.GPIO as gpio
import sys, termios, tty, os, time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(25, gpio.OUT) #IN1 Steering
    gpio.setup(22, gpio.OUT) #IN2 Steering
    gpio.setup(23, gpio.OUT) #IN3 RearEngine
    gpio.setup(24, gpio.OUT) #IN4 RearEngine

    gpio.output(25, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)

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

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0
exec_time = 0.2


while True:
    char = getch()

    if (char == "p"):
        print("Stop!")
        exit(0)

    if (char == "a"):
        print("Left pressed")
        leftForward(exec_time)
        time.sleep(button_delay)

    elif (char == "d"):
        print("Right pressed")
        rightForward(exec_time)
        time.sleep(button_delay)

    elif (char == "w"):
        print("forward")
        forward(exec_time)
        time.sleep(button_delay)

    elif (char == "s"):
        print("backward")
        reverse(exec_time)
        time.sleep(button_delay)

    elif (char == "y"):
        print("leftBackward")
        leftBackward(exec_time)
        time.sleep(button_delay)

    elif (char == "x"):
        print("rightBackward")
        rightBackward(exec_time)
        time.sleep(button_delay)

    elif (char == "t"):
        print("Getting Distance...")
        dist = getDistance()
        print ("Entfernung = %.1f cm" % dist)



print "forward"
#forward(1)
print("left")
#leftForward(1)
