import RPi.GPIO as GPIO


sensor = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
try: 
   while True:
      if GPIO.input(sensor):
          print ("Object Detected")

except KeyboardInterrupt:
    GPIO.cleanup()