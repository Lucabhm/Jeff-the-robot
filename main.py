from RPi.GPIO import GPIO
import time
import directions
GPIO.setmode(GPIO.BCM)

# Motors
## Motor 1 = front left

OUTFL0 = 17
OUTFL1 = 27
OUTFL2 = 22

## Motor 2 = back left

OUTBL0 = 23
OUTBL1 = 24
OUTBL2 = 25

## Motor 3 = front right

OUTFR0 = 5
OUTFR1 = 6
OUTFR2 = 13

## Motor 4 = back right

OUTBR0 = 12
OUTBR1 = 16
OUTBR2 = 26

PINS = [OUTFL1, OUTFL2, OUTBL1, OUTBL2, OUTFR1, OUTFR2, OUTBR1, OUTBR2]
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

PWMFL = GPIO.PWM(OUTFL0, 100)
PWMBL = GPIO.PWM(OUTBL0, 100)
PWMFR = GPIO.PWM(OUTFR0, 100)
PWMBR = GPIO.PWM(OUTBR0, 100)

PWMFL.start(0)
PWMBL.start(0)
PWMFR.start(0)
PWMBR.start(0)

print('Forward')
directions.forward(OUTFL1, OUTFL2, OUTBL1, OUTBL2, OUTFR1, OUTFR2, OUTBR1, OUTBR2)
time.sleep(5)
print('Stop')
directions.stop(PINS)
time.sleep(5)
print('Backward')
directions.backward(OUTFL1, OUTFL2, OUTBL1, OUTBL2, OUTFR1, OUTFR2, OUTBR1, OUTBR2)
time.sleep(5)
print('End')
directions.stop(PINS)
GPIO.cleanup()