import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
while True:
 val = GPIO.input(3)
 if val == 0:
    print(f"Light exceeds threshold, value is {val}")

 else:
    print(f"Light is under threshold, value is {val}")
 time.sleep(1)