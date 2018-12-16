import RPi.GPIO as gpio
import sys, termios, tty, os, time, thread, pygame #import libs
import movement, addons, distance #import local

os.system("amixer set PCM 100") #set speaker sound to 100


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
        movement.leftForward(exec_time)
        time.sleep(button_delay)

    elif (char == "d"):
        print("Right pressed")
        movement.rightForward(exec_time)
        time.sleep(button_delay)

    elif (char == "w"):
        print("forward")
        dist = distance.getDistance()

        if (dist > 20):
            movement.forward(exec_time)
        else:
            print("CRASH AVOIDED")

        time.sleep(button_delay)

    elif (char == "s"):
        print("backward")
        movement.reverse(exec_time)
        thread.start_new_thread( movement.reverse, (exec_time, ) )
        time.sleep(button_delay)

    elif (char == "y"):
        print("leftBackward")
        movement.leftBackward(exec_time)
        time.sleep(button_delay)

    elif (char == "x"):
        print("rightBackward")
        movement.rightBackward(exec_time)
        time.sleep(button_delay)

    elif (char == "t"):
        print("Getting Distance...")
        dist = distance.getDistance()
        print ("Entfernung = %.1f cm" % dist)

    elif (char == "h"):
        print("Horn...")
        thread.start_new_thread( addons.playsound, ("sounds/horn1.ogg", ) )
        #addons.playsound("sounds/horn1.ogg")

    elif (char == "i"):
        print("Ice Cream Truck Mode")
        thread.start_new_thread( addons.playsound, ("sounds/icecream.ogg", ) )
        #addons.playsound("sounds/icecream.ogg")
