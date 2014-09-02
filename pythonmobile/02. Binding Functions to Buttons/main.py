import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        btn1 = Button(text="Hello")
        btn1.bind(on_press=self.hello)
        
        btn2 = Button(text="World")
        btn2.bind(on_press=self.world)

        self.add_widget(btn1)
        self.add_widget(btn2)

    def hello(self, *args):
        print("Hello")

    def world(self, *args):
        print("World")


class KivyApp(App):
	def build(self):
		return MyWidget()


if __name__ == '__main__':
	KivyApp().run()