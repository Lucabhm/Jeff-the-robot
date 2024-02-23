from sshkeyboard import *
import sys
import directions

def	on_press(key, pin1, pin2, pin3, pin4):
	if key == "up":
		directions.forward(pin1, pin2, pin3, pin4)
	elif key == "down":
		directions.backward(pin1, pin2, pin3, pin4)
	elif key == "right":
		directions.right(pin1, pin2, pin3, pin4)
	elif key == "left":
		directions.left(pin1, pin2, pin3, pin4)

def	on_release(key, pin1, pin2, pin3, pin4):
	pins = [pin1, pin2, pin3, pin4]
	if key in ["up", "down", "right", "left"]:
		directions.stop(pins)
	elif key == "esc":
		print('Exit')
		sys.exit(0)

def	start(pin1, pin2, pin3, pin4):
	listen_keyboard(on_press=lambda key: on_press(key, pin1, pin2, pin3, pin4),
		on_release=lambda key: on_release(key, pin1, pin2, pin3, pin4))