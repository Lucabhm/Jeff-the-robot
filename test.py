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

print("forward")
d.forward(sensor, sensor1, sensor2, sensor3)
word = input()
#time.sleep(2)
d.stop([sensor, sensor1, sensor2, sensor3])
print("backward")
d.backward(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop([sensor, sensor1, sensor2, sensor3])
print("right")
d.right(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop([sensor, sensor1, sensor2, sensor3])
print("left")
d.left(sensor, sensor1, sensor2, sensor3)
time.sleep(2)
d.stop([sensor, sensor1, sensor2, sensor3])

GPIO.cleanup()
