import RPi.GPIO as GPIO

def	forward(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8):
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	GPIO.output(pin5, GPIO.HIGH)
	GPIO.output(pin6, GPIO.LOW)
	GPIO.output(pin7, GPIO.HIGH)
	GPIO.output(pin8, GPIO.LOW)

def	backward(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8):
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	GPIO.output(pin5, GPIO.LOW)
	GPIO.output(pin6, GPIO.HIGH)
	GPIO.output(pin7, GPIO.LOW)
	GPIO.output(pin8, GPIO.HIGH)

def	stop(pins):
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)