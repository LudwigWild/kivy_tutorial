import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
	pass

class KivyApp(App):
	def build(self):
		Builder.load_file('ui.kv')
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
