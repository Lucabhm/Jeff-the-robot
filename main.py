import RPi.GPIO as GPIO
import time
import directions
import manual_control
import ultrasonic_sensor as us
from multiprocessing import Process
import servo_motor as sm

GPIO.setmode(GPIO.BCM)


# Motors for wheels
## Motor 1 = front right,  Motor 3 = back right

OUT1_0 = 17
OUT1_1 = 6
OUT1_2 = 5

## Motor 2 = front left, Motor 4 = back left

OUT2_0 = 23
OUT2_1 = 24
OUT2_2 = 25

# Motor for senor

OUT3_0 = 17

# IR sensor

OUT4_0 = 26
OUT4_1 = 6

# ultrasonic sensor

OUT5_0 = 18
OUT5_1 = 16

PINS = [OUT1_1, OUT1_2, OUT2_1, OUT2_2, OUT3_0]
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(OUT3_0, 50)
p.start(6.75)
GPIO.setup(OUT5_0, GPIO.OUT)
GPIO.setup(OUT5_1, GPIO.IN)
GPIO.setup(OUT4_0, GPIO.IN)
GPIO.setup(OUT4_1, GPIO.IN)

print('Start the manual mode Y/N')
manual = input()
if manual == 'y' or manual == 'Y':
	manual_control.start(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
else:
	p1 = Process(target=sm.set_to_zero)
	pl = Process(targen=directions.left, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))
	pr = Process(targen=directions.right, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))
	try:
		while True:
			if (GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
				if (us.distanz(OUT5_0, OUT5_1) < 10):
					directions.stop(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
				else:
					directions.forward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
			# elif (GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
			# 	for i in range(6.75, 2.5, -0.25) or (GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
			# 		p.ChangeDutyCycle(i)
			# 		time.sleep(0.5)
			# 	if (us.distanz() < 10):
			# 		directions.stop(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
			# 	else:
			# 		while i < 6.75:
			# 			p1.start(OUT4_0, OUT4_1, i)
			# 			pl.start()
			# 		p1.join()
			# 		pl.join()
			# elif (not GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
			# 	for i in range(6.75, 12.5, 0.25) or (not GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
			# 		p.ChangeDutyCycle(i)
			# 		time.sleep(0.5)
			# 	if (us.distanz() < 10):
			# 		directions.stop(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
			# 	else:
			# 		while i > 6.75:
			# 			p1.start(OUT4_0, OUT4_1, i)
			# 			pr.start()
			# 		p1.join()
			# 		pr.join()
	except KeyboardInterrupt:
		p.stop()
GPIO.cleanup()
