import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout


class RootWidget(GridLayout):
	pass

class KivyApp(App):
	def build(self):
		Builder.load_file('ui1.kv')	# other: 'ui2.kv'
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
