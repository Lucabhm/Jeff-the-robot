from pynput.keyboard import *
import sys
import directions

def	on_press(key, pin1, pin2, pin3, pin4):
	if key == Key.up:
		print('up')
		directions.forward(pin1, pin2, pin3, pin4)
	elif key == Key.down:
		print('down')
		directions.backward(pin1, pin2, pin3, pin4)
	elif key == Key.right:
		print('right')
		directions.right(pin1, pin2, pin3, pin4)
	elif key == Key.left:
		print('left')
		directions.left(pin1, pin2, pin3, pin4)

def	on_release(key, pin1, pin2, pin3, pin4):
	if key in [Key.up, Key.down, Key.right, Key.left]:
		directions.stop(pin1, pin2, pin3, pin4)
	elif key == Key.esc:
		print('Exit')
		sys.exit(0)

def	start(pin1, pin2, pin3, pin4):
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()
