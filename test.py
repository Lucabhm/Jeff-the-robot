import RPi.GPIO as GPIO
import directions as d
import time

sensor = 6
sensor1 = 13
sensor2 = 19
sensor3 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor,GPIO.OUT)
GPIO.setup(sensor1,GPIO.OUT)
GPIO.setup(sensor2,GPIO.OUT)
GPIO.setup(sensor3,GPIO.OUT)

d.forward(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop(sensor, sensor1, sensor2, sensor3)
d.backward(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop(sensor, sensor1, sensor2, sensor3)
d.right(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop(sensor, sensor1, sensor2, sensor3)
d.left(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop(sensor, sensor1, sensor2, sensor3)

GPIO.cleanup()
