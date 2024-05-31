import RPi.GPIO as GPIO
import time

servoPIN = 17
i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(i)
for i in range(0, 12.5, 0.25):
	p.ChangeDutyCycle(i)
for i in range(12.5, 0, -0.25):
	p.ChangeDutyCycle(i)

GPIO.cleanup()