# Eto kommentari. Python ego ignoriruyet, tak chto mozhno pisat' vse 
# chto hochesh. Knopka kozyavka =P.

from RPi import GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)

ports = [11, 16, 22]
status = [0, 0, 0] # 0 esli vykluchen port, 1 esli vkluchen. Iznachal'no vse OFF


for i in ports:
	GPIO.setup(i, GPIO.OUT)

# random.random() generiruyet sluchainoye chislo ot [0.0, 1.0)

for w in range (1,100):
	r = int(random.random() * 3) # int(x) convertiruyet x v celoye chislo. Vybirayem sluchainyi port.
	if random.random() < 0.5: # vypal 'orel'
		if status[r] == 0: # esli OFF, vklcuhit' tok
			status[r] = 1
			GPIO.output(ports[r], GPIO.HIGH)
		else: # esli ON, vykluchit tok
			status[r] = 0
			GPIO.output(ports[r], GPIO.LOW)
	time.sleep(0.1) # pospat 100 ms
GPIO.cleanup()

