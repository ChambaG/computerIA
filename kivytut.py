from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class ButtonsApp(App, FloatLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ButtonsApp().run()
