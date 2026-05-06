import RPi.GPIO as GPIO

import random
import time

BUTTON_PIN=17
LCD_ADDRESS = 0x27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
start = ("000")
timestorepeat = (20)

def wait_for_button():
    """
    Wait until button is pressed.
    """
    while GPIO.input(17) == GPIO.HIGH:
       time.sleep(0.01)
        
    while GPIO.input(17) == GPIO.LOW:
        time.sleep(0.01)
        
        time.sleep(0.2)
        

try:
    while True:
        print("000")
        
        wait_for_button()
        
        while timestorepeat > 0:
            numout = random.randint(101,999)
            print(numout)
            numout = random.randint(101,999)
            time.sleep(0.08)
            print("\033[A                             \033[A")
            timestorepeat -=1
        print(numout)
        wait_for_button()
        
except KeyboardInterrupt:
    pass
 
finally:
    GPIO.cleanup()



      
