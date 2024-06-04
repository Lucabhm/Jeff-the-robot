import RPi.GPIO as GPIO
import time

servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(12.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(2.5)
		time.sleep(0.5)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

def set_to_zero(pin1, pin2, i):
	if (i < 6.75):
		for i in range(i, 6.75, 0,25) and not GPIO.input(pin1) and GPIO.input(pin2):
			p.ChangeDutyCycle(i)
			time.sleep(0.5)
	else:
		for i in range(i, 6.75, -0,25) and GPIO.input(pin1) and not GPIO.input(pin2):
			p.ChangeDutyCycle(i)
			time.sleep(0.5)
