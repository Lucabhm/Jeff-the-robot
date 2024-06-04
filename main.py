import RPi.GPIO as GPIO
import time
import directions
import manual_control
import ultrasonic_sensor as us
import multiprocessing
import servo_motor as sm
GPIO.setmode(GPIO.BCM)


# Motors for wheels
## Motor 1 = front right,  Motor 3 = back right

OUT1_1 = 6
OUT1_2 = 13

## Motor 2 = front left, Motor 4 = back left

OUT2_1 = 19
OUT2_2 = 26

# Motor for senor

OUT3_0 = 12

# IR sensor

OUT4_0 = 23 # left
OUT4_1 = 24 # right

# ultrasonic sensor

OUT5_0 = 18
OUT5_1 = 25

PINS = [OUT1_1, OUT1_2, OUT2_1, OUT2_2]
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)
GPIO.setup(OUT3_0, GPIO.OUT)
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
	distanz_val = 0
	i = 6.5
	queue = multiprocessing.Queue()
	p2 = multiprocessing. Process(target=us.distanz, args=(queue, OUT5_0, OUT5_1))
	p2.start()
#	p1 = Process(target=sm.set_to_zero)
#	pl = Process(target=directions.left, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))
#	pr = Process(target=directions.right, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))
	try:
		print("forward")
		directions.forward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
		time.sleep(5)
		print("stop")
		directions.stop([OUT1_1, OUT1_2, OUT2_1, OUT2_2])
		while True:
#			if (not GPIO.input(OUT4_0)):
#				print("left")
#			if (not GPIO.input(OUT4_1)):
#				print("right")
			if (not GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
				print("here")
				while not GPIO.input(OUT4_0) and not GPIO.input(OUT4_1):
					print("inside loop")
					distanz_val = queue.get()
					print("distanz = %.1f" % distanz_val)
					if (distanz_val < 10):
						print("stop")
						directions.stop([OUT1_1, OUT1_2, OUT2_1, OUT2_2])
					else:
						print("forward")
						directions.forward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
					time.sleep(0.5)
			elif (GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
			 	#for i in range(7, 2, -1) or (GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
				while (i >= 2.5 and GPIO.input(OUT4_0) and not GPIO.input(OUT4_1)):
					p.ChangeDutyCycle(i)
					time.sleep(0.1)
					i -= 0.5
			# 	if (us.distanz() < 10):
			# 		directions.stop(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
			# 	else:
			# 		while i < 6.75:
			# 			p1.start(OUT4_0, OUT4_1, i)
			# 			pl.start()
			# 		p1.join()
			# 		pl.join()
			elif (not GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
			 	#for i in range(7, 12, 1) or (not GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
				while (i <= 12.5 and not GPIO.input(OUT4_0) and GPIO.input(OUT4_1)):
					p.ChangeDutyCycle(i)
					time.sleep(0.1)
					i += 0.5
			# 	if (us.distanz() < 10):
			# 		directions.stop(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
			# 	else:
			# 		while i > 6.75:
			# 			p1.start(OUT4_0, OUT4_1, i)
			# 			pr.start()
			# 		p1.join()
			# 		pr.join()
	except KeyboardInterrupt:
		p2.join()
		p.stop()
		GPIO.cleanup()
GPIO.cleanup()
p2.join()
