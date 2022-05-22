from time import time
import RPi.GPIO as GPIO
import rgb
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
temperature = sensor.get_temperature()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
IR_PIN1=15
IR_PIN2=16
GPIO.setup(IR_PIN1, GPIO.IN)
GPIO.setup(IR_PIN2, GPIO.IN)
GPIO.setup(19, GPIO.OUT)

while True:
    rgb.red()#紅燈
    print(temperature)
    val1 = GPIO.input(IR_PIN1)
    val2 = GPIO.input(IR_PIN2)
    print(f"IR value is {val1}")
    print(f"IR value is {val2}")
    if val1 == 0 and temperature > 21.0 :  #紅外線與溫度
        rgb.blue()

        for i in range(1000):
            for j in range(250):
                GPIO.output(19, 1)
            for j in range(1000):#聲音的平率
                GPIO.output(19, 0)#蜂鳴器街腳
    
    if val2 == 0 :  
        rgb.blue()

        for i in range(1000):#下一首
            for j in range(250):
                GPIO.output(19, 1)
            for j in range(250):
                GPIO.output(19, 0)
        
        
     
    
        
        
