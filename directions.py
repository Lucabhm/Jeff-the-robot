import RPi.GPIO as GPIO

def	forward(pin1, pin2, pin3, pin4):
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)

def	backward(pin1, pin2, pin3, pin4):
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)


def	right(pin1, pin2, pin3, pin4):
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)

def	left(pin1, pin2, pin3, pin4):
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)

def	stop(pins):
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)