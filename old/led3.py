from RPi import GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)



for w in range (1,10):
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(16,GPIO.HIGH)
	time.sleep (1)
	GPIO.output(11,GPIO.LOW)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	time.sleep (1)
GPIO.cleanup()
