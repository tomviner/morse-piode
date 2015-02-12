import pibrella as p
import time
import sys

def render_morse(s):
	print(s)

def press(pin):
	print(pin.read())

class Button(object):
	def __init__(self):
		self.pressed = False
		self.last_pressed_at = None
		p.button.changed(self.press)

	def press(self, pin):
		if self.pressed:
			duration = time.time() - self.last_pressed_at
			self.up(duration)
			self.last_pressed_at = None
		else:
			self.down()
			self.last_pressed_at = time.time()
		self.pressed = pin.read()

	def down(self):
		p.buzzer.note(3)

	def up(self, duration):
		p.buzzer.off()
		if duration > .3:
			print('-', end='')
		else:
			print('.', end='')
		sys.stdout.flush()

	
if __name__ == '__main__':
	button = Button()
	while True:
		time.sleep(0.01)
