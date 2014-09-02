import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button


class KivyApp(App):
	def build(self):
		return Button(text="Hello World")


KivyApp().run()