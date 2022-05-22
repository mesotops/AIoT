import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.add_event_detect(12, GPIO.FALLING)
while True:
 '''
 if GPIO.input(12) == 0:
 print("status is 0")
 else:
 print("status is 1")
 '''
 if GPIO.input(12) == 1:

    print("off")
 if GPIO.event_detected(12):
    print("button pressed-on")
 time.sleep(0.5)
