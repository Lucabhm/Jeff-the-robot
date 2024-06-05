import RPi.GPIO as GPIO
import time
import multiprocessing

distanz_test = 0

def distanz(GPIO_TRIGGER, GPIO_ECHO):
	print("start distanz")
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	StartZeit = time.time()
	StopZeit = time.time()
	while GPIO.input(GPIO_ECHO) == 0:
			StartZeit = time.time()
	while GPIO.input(GPIO_ECHO) == 1:
			StopZeit = time.time()
	TimeElapsed = StopZeit - StartZeit
	distanz_test = (TimeElapsed * 34300) / 2
	print ("Gemessene Entfernung = %.1f cm" % distanz_test)
	return (distanz_test)
