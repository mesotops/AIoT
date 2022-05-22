import time  # 匯入時間模組
import RPi.GPIO as GPIO  # 匯入RPi.GPIO 模組, 使⽤別名 GPIO
GPIO.setwarnings(False)  # 在執⾏的過程中將所有的警告訊息關閉
GPIO.setmode(GPIO.BOARD)  # BCM mode: 為使⽤CPU定義的數字, BORAD: 為使⽤實體(板⼦)上的數字.

GPIO.setup(29, GPIO.OUT)  # 設定板⼦上的第三位腳位為輸出模式
GPIO.setup(31, GPIO.OUT)  # 設定板⼦上的第五位腳位為輸出模式
GPIO.setup(33, GPIO.OUT)  # 設定板⼦上的第七位腳位為輸出模式

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