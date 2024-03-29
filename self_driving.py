import RPi.GPIO as GPIO
import time
import directions
import manual_control

GPIO.setmode(GPIO.BCM)

OUT1_1 = 27
OUT1_2 = 22

GPIO.output(OUT1_1, GPIO.LOW)
GPIO.output(OUT1_2, GPIO.HIGH)
time.sleep(3)
GPIO.output(OUT1_1, GPIO.LOW)
GPIO.output(OUT1_2, GPIO.LOW)
GPIO.cleanup()