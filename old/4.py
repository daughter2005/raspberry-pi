from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


for t in range (1,10):
	GPIO.output(11, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(16, GPIO.HIGH)
	time.sleep (1)
	GPIO.output(11, GPIO.LOW)
	time.sleep(1)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(16, GPIO.LOW)
	time.sleep (1)
	GPIO.output(11, GPIO.HIGH)
	time.sleep (1)
	GPIO.output(22, GPIO.LOW)
	time.sleep (1)
	GPIO.output(11, GPIO.LOW)
GPIO.cleanup()

