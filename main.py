import RPi.GPIO as GPIO
import time
import directions
GPIO.setmode(GPIO.BCM)

# Motors
## Motor 1 = front left,  Motor 3 = back left

OUT1_3_0 = 17
OUT1_3_1 = 27
OUT1_3_2 = 22

## Motor 2 = front right, Motor 4 = back right

OUT2_4_0 = 23
OUT2_4_1 = 24
OUT2_4_2 = 25

PINS = [OUT1_3_1, OUT1_3_2, OUT2_4_1, OUT2_4_2]
PWMS = [OUT1_3_0, OUT2_4_0]
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

for pwm in PWMS:
	GPIO.setup(pwm, GPIO.OUT)
PWMFL = GPIO.PWM(OUT1_3_0, 100)
PWMBL = GPIO.PWM(OUT2_4_0, 100)

PWMFL.start(0)
PWMBL.start(0)

print('Forward')
directions.forward(OUT1_3_1, OUT1_3_2, OUT2_4_1, OUT2_4_2)
time.sleep(3)
print('Stop')
directions.stop(PINS)
time.sleep(3)
print('Backward')
directions.backward(OUT1_3_1, OUT1_3_2, OUT2_4_1, OUT2_4_2)
time.sleep(3)
print('Stop')
directions.stop(PINS)
time.sleep(3)
print('Right')
directions.right(OUT1_3_1, OUT1_3_2, OUT2_4_1, OUT2_4_2)
time.sleep(3)
print('Stop')
directions.stop(PINS)
time.sleep(3)
print('Left')
directions.left(OUT1_3_1, OUT1_3_2, OUT2_4_1, OUT2_4_2)
time.sleep(3)
print('End')
directions.stop(PINS)
GPIO.cleanup()