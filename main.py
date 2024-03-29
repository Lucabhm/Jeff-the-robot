import RPi.GPIO as GPIO
import time
import directions
import manual_control

GPIO.setmode(GPIO.BCM)

# Motors for wheels
## Motor 1 = front right,  Motor 3 = back right

OUT1_0 = 17
OUT1_1 = 27
OUT1_2 = 22

## Motor 2 = front left, Motor 4 = back left

OUT2_0 = 23
OUT2_1 = 24
OUT2_2 = 25

# Motor for senor

OUT3_0 = 4

# IR sensor

OUT4_0 = 5
OUT4_1 = 6

# ultrasonic sensor

OUT5_0 = 12
OUT5_1 = 16

PINS = [OUT1_1, OUT1_2, OUT2_1, OUT2_2]
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

print('Start the manual mode Y/N')
manual = input()
if manual == 'y' or manual == 'Y':
	manual_control.start(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
else:
	print('Forward')
	directions.forward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
	time.sleep(3)
	print('Stop')
	directions.stop(PINS)
	time.sleep(3)
	print('Backward')
	directions.backward(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
	time.sleep(3)
	print('Stop')
	directions.stop(PINS)
	time.sleep(3)
	print('Right')
	directions.right(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
	time.sleep(3)
	print('Stop')
	directions.stop(PINS)
	time.sleep(3)
	print('Left')
	directions.left(OUT1_1, OUT1_2, OUT2_1, OUT2_2)
	time.sleep(3)
	print('End')
	directions.stop(PINS)
GPIO.cleanup()