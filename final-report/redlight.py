import RPi.GPIO as GPIO
import time
IR_PIN = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_PIN, GPIO.IN)
while True:
    val = GPIO.input(IR_PIN)
    print(f"IR value is {val}")
    if val == 0:
        print("Obstacle")
    else:
        print("clear")
    time.sleep(0.5)
