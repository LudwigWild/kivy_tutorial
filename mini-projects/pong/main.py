import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

import random


class Ball(Widget):
	pass


class Racket(Widget):
	pass
	

class PongGame(FloatLayout):
	pass


class KivyApp(App):
	def build(self):
		self.title = "Pong"
		Builder.load_file('ui.kv')
		return PongGame()


if __name__ == '__main__':
	KivyApp().run()
