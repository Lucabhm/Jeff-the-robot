import RPi.GPIO as GPIO
import time
import directions
import manual_control
import ultrasonic_sensor as us
import multiprocessing
import servo_motor as sm

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Motors for wheels
## Motor 1 = front right, Motor 3 = back right
OUT1_1 = 6
OUT1_2 = 13

## Motor 2 = front left, Motor 4 = back left
OUT2_1 = 19
OUT2_2 = 26

# Motor for sensor
OUT3_0 = 12

# IR sensor
OUT4_0 = 23  # left
OUT4_1 = 24  # right

# ultrasonic sensor
OUT5_0 = 17
OUT5_1 = 25

GPIO.setup(OUT1_1, GPIO.OUT)
GPIO.setup(OUT1_2, GPIO.OUT)
GPIO.setup(OUT2_1, GPIO.OUT)
GPIO.setup(OUT2_2, GPIO.OUT)
GPIO.setup(OUT5_0, GPIO.OUT)
GPIO.setup(OUT5_1, GPIO.IN)
GPIO.setup(OUT4_0, GPIO.IN)
GPIO.setup(OUT4_1, GPIO.IN)

print('Start the manual mode Y/N')
manual = input()
if manual == 'y' or manual == 'Y':
	try:
		manual_control.start(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
	finally:
		GPIO.cleanup()
else:
	GPIO.setup(OUT3_0, GPIO.OUT)
	distanz_val = 0
	i = 7.5
	p = GPIO.PWM(OUT3_0, 50)
	p.start(i)
	queue = multiprocessing.Queue()
	# Uncomment and correctly define processes if needed
	# p1 = multiprocessing.Process(target=sm.set_to_zero)
	# pl = multiprocessing.Process(target=directions.left, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))
	# pr = multiprocessing.Process(target=directions.right, args=(OUT1_1, OUT1_2, OUT2_1, OUT2_2))

	try:
		while True:
			if not GPIO.input(OUT4_0) and not GPIO.input(OUT4_1):
				while not GPIO.input(OUT4_0) and not GPIO.input(OUT4_1):
					distanz_val = us.distanz(OUT5_0, OUT5_1)
					if distanz_val <= 10:
						print("stop")
						directions.stop([OUT1_1, OUT1_2, OUT2_1, OUT2_2])
					else:
						print("forward")
						directions.forward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
					time.sleep(0.5)
			elif GPIO.input(OUT4_0) and not GPIO.input(OUT4_1):
				directions.left(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
				while GPIO.input(OUT4_0) and not GPIO.input(OUT4_1):
					print("left")
					time.sleep(0.5)
			elif not GPIO.input(OUT4_0) and GPIO.input(OUT4_1):
				directions.right(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
				while not GPIO.input(OUT4_0) and GPIO.input(OUT4_1):
					print("right")
					time.sleep(0.5)
			directions.stop([OUT1_1, OUT1_2, OUT2_1, OUT2_2])
	except KeyboardInterrupt:
		p.stop()
		directions.stop([OUT1_1, OUT1_2, OUT2_1, OUT2_2])
	finally:
		GPIO.cleanup()
