import kivy
import main
kivy.require('1.10.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.floatlayout import FloatLayout


class MainScreen(Screen, FloatLayout):

    auction_name = " "
    x_value = 450
    y_value = 500

    @classmethod
    def start_process(cls):
        if cls.auction_name != " ":
            main.run()

    @classmethod
    def select(cls, auction_name):
        print("Yes")
        cls.auction_name = auction_name

    pass


class LoadingScreen(Screen):
    pass


class ResultScreen(Screen, FloatLayout):
    pass


class ScreenManagement(ScreenManager):
    pass


class MainApp(App):

    choice = ""

    def build(self):
        main_window = Builder.load_file("main.kv")
        return main_window


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (450, 500)
    MainApp().run()




