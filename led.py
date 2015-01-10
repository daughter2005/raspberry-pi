from RPi import GPIO
import time

led = 16
print ('Turning %s port, GPIO.HIGH = %s' % (led, GPIO.HIGH))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, GPIO.HIGH)
time.sleep(4)
GPIO.cleanup()
