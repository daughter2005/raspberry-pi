from RPi import GPIO
import time

newled = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(newled, GPIO.OUT)
GPIO.output(newled, GPIO.HIGH)
w=raw_input('press any key')
GPIO.cleanup()
