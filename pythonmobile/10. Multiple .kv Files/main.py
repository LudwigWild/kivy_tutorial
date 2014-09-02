import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
	pass

class KivyApp(App):
	def build(self):
		Builder.load_file('./kv/VioletAnchor.kv')
		Builder.load_file('./kv/WhiteAnchor.kv')
		Builder.load_file('./kv/SmallButton.kv')
		Builder.load_file('./kv/RootWidget.kv')

		# We create two vars that will be accessible from the .kv files
		# by using 'app.x_relat' and 'app.y_relat' (e.g. SmallButton.kv).
		self.x_relat = 0.2
		self.y_relat = 0.4
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
