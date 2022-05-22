import uuid
from bluetooth import *
import RPi.GPIO as GPIO
from time import time
# import rgb
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
temperature = sensor.get_temperature()
 
# LED_PIN = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
IR_PIN1=15
IR_PIN2=16
GPIO.setup(IR_PIN1, GPIO.IN)
GPIO.setup(IR_PIN2, GPIO.IN)
GPIO.setup(19, GPIO.OUT)

def red():
    GPIO.output(29, 1)  # 設定板⼦上的第三位腳位輸出⾼電位(3.3V)
    GPIO.output(31, 0)  # 設定板⼦上的第五位腳位輸出低電位(0V)
    GPIO.output(33, 0)

   
def green():
    GPIO.output(29, 0)  # 設定板⼦上的第三位腳位輸出低電位
    GPIO.output(31, 1)  # 設定板⼦上的第五位腳位輸出⾼電位
    GPIO.output(33, 0)

   
def blue():
    GPIO.output(29, 0)  # 設定板⼦上的第三位腳位輸出低電位
    GPIO.output(31, 0)  # 設定板⼦上的第五位腳位輸出⾼電位
    GPIO.output(33, 1)
 
server_socket=BluetoothSocket(RFCOMM)
server_socket.bind(("", PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
service_id = str(uuid.uuid4())
 
advertise_service(server_socket, "LEDServer",
                  service_id = service_id,
                  service_classes = [service_id, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE])
 
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        print('等待 RFCOMM 頻道 {} 的連線'.format(port))
        client_socket, client_info = server_socket.accept()
        print('接受來自 {} 的連線'.format(client_info))
        try:
            while True:
            #     data = client_socket.recv(1024).decode().lower()
            #     if len(data) == 0:
            #         break
            #     if data == 'on':
            #         GPIO.output(LED_PIN, GPIO.HIGH)
            #         print('開燈')
            #     elif data == 'off':
            #         GPIO.output(LED_PIN, GPIO.LOW)
            #         print('關燈')
            #     else:
            #         print('未知的指令: {}'.format(data))
                red()#紅燈
                print(temperature)
                val1 = GPIO.input(IR_PIN1)
                val2 = GPIO.input(IR_PIN2)
                print(f"IR value is {val1}")
                print(f"IR value is {val2}")
                if val1 == 0 and temperature > 21.0 :  #紅外線與溫度
                    blue()

                    for i in range(1000):
                        for j in range(250):
                            GPIO.output(19, 1)
                        for j in range(1000):#聲音的頻率
                            GPIO.output(19, 0)#蜂鳴器接腳
                
                if val2 == 0 :  
                    blue()

                    for i in range(1000):#下一首
                        for j in range(250):
                            GPIO.output(19, 1)
                        for j in range(250):
                            GPIO.output(19, 0)
        except IOError:
            pass
        client_socket.close()
        print('中斷連線')
except KeyboardInterrupt:
    print('中斷程式')
finally:
    if 'client_socket' in vars():
        client_socket.close()
    server_socket.close()
    GPIO.cleanup()
    print('中斷連線')