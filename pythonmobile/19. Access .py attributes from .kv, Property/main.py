import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

import random


class RootWidget(BoxLayout):
	# This attribute has to be a class variable if we want to access it from the .kv files.
	# If we create this attribute as an instance variable (e.g.: self.random_color within
	# a __init__() constructor method), we won't be able to access this attribue from
	# the .kv files.

	random_color = ListProperty([0.4, 0.5, 0.6, 1])

	# If this attribute get modified by a method, the value accessed from the .kv file won't
	# reflect this change, the value seen from the .kv file will still be the previous one.
	# We could make an instrution (using self.ids['<id>'].<attribute>) within the method,
	# just after the attribute's value modification, to access the concerned attribute of
	# the .kv file and manually assign it the new modified value ; but it would be cumbersome
	# if several .kv attributes needed to access to this .py attribute.
	#
	# A better solution is to use the Kivy Property instruction : if the attribute use
	# the Property instruction, each modification you make on its value will be automatically
	# reflected in the value seen from the .kv file.
	#
	# Whenever you create a Property, Kivy automatically creates a method on_<property>(),
	# in this case: on_random_color(), that you can define in the class.
	# This method will be automatically called each time the value of the attribute is modified.

	def change_color(self, *args):
		"""
		Pick a random color and assign it to the random_color attribute.
		"""
		self.random_color = [random.random() for i in range(3)] + [1]
		

class KivyApp(App):
	def build(self):
		Builder.load_file('ui.kv')
		self.title = "Access .py attributes from .kv, Property"
		return RootWidget()


if __name__ == '__main__':
	KivyApp().run()
