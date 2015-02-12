import pibrella as p
import time
import sys
import os
from pprint import pprint

from data import morse
pprint(morse)
def render_morse(s):
	print(s)

def press(pin):
	print(pin.read())

class Button(object):
	def __init__(self):
		self.pressed = False
		self.last_pressed_at = time.time()
		self.last_upped_at = time.time()
		p.button.changed(self.press)
		self.message = ''
		self.all = ''

	def press(self, pin):
		if not pin.read():
			self.last_upped_at = time.time()
			duration = time.time() - self.last_pressed_at
			self.up(duration)
			self.last_pressed_at = time.time()
		else:
			self.last_pressed_at = time.time()
			duration_up = time.time() - self.last_upped_at
			self.down(duration_up)

	def down(self, duration_up):
		if duration_up > 0.7:
			if self.message in morse or len(self.message)>4:
				os.system('clear')
				letter = morse[self.message]
				self.all += letter
				print(self.all)
			
			self.message = ''
		p.buzzer.note(3)

	def up(self, duration):
		p.buzzer.off()
		if duration > .1:
			letter = '-'
		else:
			letter = '.'
		self.message += letter
		print(letter, end='')
		sys.stdout.flush()
		
		

	
if __name__ == '__main__':
	button = Button()
	while True:
		time.sleep(0.01)
