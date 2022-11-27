from tkinter import*
import tkinter.font 
from gpiozero import LED
import RPi.GPIO 

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM) 

# LED PINS
white_Led = LED (20)
red_Led = LED (16)
blue_Led = LED (21)

# OPEN WINDOW
win = Tk()
win.title("CONTROL LEDS")
myFont = tkinter.font. Font(family = 'Helvetica', size = 11, weight = "bold")
count = IntVar()

# FUNCTIONS FOR LED CONTROL
def WhiteLED():
    if white_Led.is_lit:
        white_Led.off()
        whiteLedButton["text"] = "Turn on White LED"

    else:
        white_Led.on()
        whiteLedButton["text"] = "Turn off White LED"
        red_Led.off()
        redLedButton["text"] = "Turn on Red LED"
        blue_Led.off()
        blueLedButton["text"] = "Turn on Blue LED"


def RedLED():

    if red_Led.is_lit:
        red_Led.off()
        redLedButton["text"] = "Turn on Red LED"

    else:
        red_Led.on()
        redLedButton["text"] = "Turn off Red LED"
        white_Led.off()
        whiteLedButton["text"] = "Turn on White LED"
        blue_Led.off()
        blueLedButton["text"] = "Turn on Blue LED"


def BlueLED():

    if blue_Led.is_lit:
        blue_Led.off()
        blueLedButton["text"] = "Turn on Blue LED"

    else:
        blue_Led.on()
        blueLedButton["text"] = "Turn off Blue LED"
        white_Led.off()
        whiteLedButton["text"] = "Turn on White LED"
        red_Led.off()
        redLedButton["text"] = "Turn on Red LED"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


# WIDGETS
whiteLedButton = Button (win, text = 'Turn on White LED', font = myFont, command = WhiteLED, bg = 'white', height = 1, width = 23)
whiteLedButton.grid (row=0, column=1)

redLedButton = Button (win, text = 'Turn on Red LED', font = myFont, command = RedLED, bg = 'red', height = 1, width = 23)
redLedButton.grid (row=1, column=1)

blueLedButton = Button (win, text = 'Turn on Blue LED', font = myFont, command = BlueLED, bg = 'blue', height = 1, width = 23)
blueLedButton.grid (row=2, column=1)

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'green', height = 1, width = 6)
exitButton.grid (row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) 
win.mainloop() 