import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

import random


class RootWidget(BoxLayout):
	def change_rectangle_color(self, *args):
		"""
		Pick a random color and assign it to the .text Labels attributes.
		"""
		random_color = [random.random() for i in range(3)] + [1]

		self.my_label1.color = random_color
		self.my_label2.color = random_color
		self.my_label3.color = random_color
		self.my_label4.color = random_color

class KivyApp(App):
	def build(self):
		Builder.load_file('method2.kv')
		self.title = "Access .kv attributes from .py"
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
