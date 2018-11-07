import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class CustomWidget(Widget):
    pass


class FloatingApp(App):

    def build(self):
        return CustomWidget()

