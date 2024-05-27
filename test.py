import RPi.GPIO as GPIO


sensor = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
print("start")
try: 
   while True:
      if not GPIO.input(sensor):
          print ("Object Detected")

except KeyboardInterrupt:
    GPIO.cleanup()
