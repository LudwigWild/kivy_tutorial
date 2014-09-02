import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import ListProperty

import random


class RootWidget(FloatLayout):
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		# No need to make this attribute a class variable because we won't need to access
		# it from the .kv file, we'll only work with it within this .py file, therefore
		# creating an instance variable is enough for our purpose.
		self.velocity = [random.randint(-10, 10), random.randint(-10, 10)]

	randomized_color = ListProperty([0.7, 0.7, 0.4, 1])

	def move_ball(self, *args):
		"""
		Moves the ball to its t+1 position according to its velocity.
		If the ball hits a wall, change velocity direction and change
		the background color.
		"""
		self.ball.x += self.velocity[0]
		self.ball.y += self.velocity[1]

		if self.ball.x < 0 or self.ball.right > self.width:
			self.velocity[0] *= -1
			self.randomize_color()
		if self.ball.y < 0 or self.ball.top > self.height:
			self.velocity[1] *= -1
			self.randomize_color()

	def randomize_color(self, *args):
		"""
		Picks a random color and assign it to the 'randomized_color'
		class attribute.
		"""
		self.randomized_color = [random.random() for i in range(3)] + [1]

	def start_ball_animation(self, *args):
		"""
		Starts the ball animation by calling the move_ball()
		method 60 times/sec.
		"""
		Clock.schedule_interval(self.move_ball, 1.0/60)


class KivyApp(App):
	def build(self):
		self.title = "Ball Animation"
		Builder.load_file('ui.kv')
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
