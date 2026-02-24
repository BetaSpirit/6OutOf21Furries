#import RPi.GPIO as GPIO
#from RPLCD.i2c import CharLCD
import random
import time
# -----------------------
# Configuration
# -----------------------
#BUTTON_PIN = 17 # unknown at the moment until I get my hands on the RPi
#LCD_ADDRESS = 0x27  # Change when screen decided.

# -----------------------
# GPIO Setup
# -----------------------
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
start = ("000")

print(start)
time.sleep(2)
print("\033[A                             \033[A")

timestorepeat = (20)

#try: 
# while true
#timestorepeat = (20)
while timestorepeat > 0:
     value = random.randint(101, 999)
     print(value)
     value = random.randint(101, 999)
     time.sleep(0.05)
     print("\033[A                             \033[A")
     timestorepeat -= 1

print(value)

#except 
#pass
# repeat back to initial clause until button pressed
#

#finally 
#time.sleep(340)
#lcd.clear
#GPIO.cleanup



