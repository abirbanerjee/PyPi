from gpiozero import LED, PWMLED, LightSensor, Buzzer, Pin
from signal import pause
import time
import os

os.system("pinout")
prog = 0
pin_no = int(input("Choose Pin, Enter GPIO number:"))

iochooser = int(input("Enter 0 for output, 1 for input:"))

if iochooser == 0:
    func = int(input("Enter choice (0.LED/1.PWMLED/2.BUZZER):"))
    if func == 0:
        led = LED(pin_no)
        while(prog != 4):
            prog = int(input("Enter 0 to turn on, 1 to off, 2 to blink, 3 to toggle,4 to exit:"))
            if prog == 0:
                led.on()
            if prog == 1:
                led.off()
            if prog == 2:
                led.blink()
            if prog == 3:
                led.toggle()
    if func == 1:
        led = PWMLED(pin_no)
        while(prog!=2):
            prog = int(input("Enter 0 to enter value of LED or enter 1 to pulsate, 2 to exit:"))
            if(prog == 0):
                led_val = float(input("Enter value between 0 to 1:"))
                led.value = led_val
            if(prog == 1):
                led.pulse()
    if func == 2:
        led = Buzzer(pin_no)
        while(prog!=3):
            prog = int(input("Enter 0 to turn on, 1 to turn off, 2 to beep, 3 to exit:"))
            if(prog == 0):
                led.on()
            if(prog == 1):
                led.off()
            if(prog == 2):
                noftimes = int(input("Enter number of beeps:"))
                led.beep(n=noftimes)
led.close()