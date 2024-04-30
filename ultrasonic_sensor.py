import RPi.GPIO as GPIO
import time

def distanz(GPIO_TRIGGER, GPIO_ECHO):
		# setze Trigger auf HIGH
		GPIO.output(GPIO_TRIGGER, True)
		# setze Trigger nach 0.01ms aus LOW
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER, False)
		StartZeit = time.time()
		StopZeit = time.time()
		# speichere Startzeit
		while GPIO.input(GPIO_ECHO) == 0:
				StartZeit = time.time()
		# speichere Ankunftszeit
		while GPIO.input(GPIO_ECHO) == 1:
				StopZeit = time.time()
		# Zeit Differenz zwischen Start und Ankunft
		TimeElapsed = StopZeit - StartZeit
		# mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
		# und durch 2 teilen, da hin und zurueck
		distanz = (TimeElapsed * 34300) / 2
		print ("Gemessene Entfernung = %.1f cm" % distanz)
		return distanz

# def distanz(GPIO_TRIGGER, GPIO_ECHO):
#     # setze Trigger auf HIGH
#     GPIO.output(GPIO_TRIGGER, True)
 
#     # setze Trigger nach 0.01ms aus LOW
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)
 
#     StartZeit = time.time()
#     StopZeit = time.time()
 
#     # speichere Startzeit
#     while GPIO.input(GPIO_ECHO) == 0:
#         StartZeit = time.time()
 
#     # speichere Ankunftszeit
#     while GPIO.input(GPIO_ECHO) == 1:
#         StopZeit = time.time()
 
#     # Zeit Differenz zwischen Start und Ankunft
#     TimeElapsed = StopZeit - StartZeit
#     # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
#     # und durch 2 teilen, da hin und zurueck
#     distanz = (TimeElapsed * 34300) / 2
 
#     return distanz
 
# if __name__ == '__main__':
#     try:
#         while True:
#             abstand = distanz()
#             print ("Gemessene Entfernung = %.1f cm" % abstand)
#             time.sleep(1)
 
#         # Beim Abbruch durch STRG+C resetten
#     except KeyboardInterrupt:
#         print("Messung vom User gestoppt")
#         GPIO.cleanup()