import kivy

kivy.require('1.10.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image


class MainScreen(Screen, FloatLayout):

    auction_name = " "
    selected_auction = StringProperty('Select an auction')
    x_value = 450
    y_value = 500

    def start_process(self):
        if self.auction_name != " ":
            print("Start the process")

    def change_label(self, change):
        if self.selected_auction == 'Selected: Copart' or self.selected_auction == 'Selected: IAAI':
            self.selected_auction = 'Selected: Copart and IAAI'
        else:
            self.selected_auction = 'Selected: {}'.format(change)
        print(self.selected_auction)


class LoadingScreen(Screen):

    def printEsc(self):
        print("IT WORKS!")

    def cancel(self):
        box = BoxLayout(orientation='vertical')
        padding = Label(text= "If you say yes all progress will be lost!")
        buttons = BoxLayout()
        warning = Image(source="Data/warning.png")
        yes_button = Button(text= "Yes, do cancel it.", size=(250, 120), background_color=(300, 0.5, 0, .7))
        no_button = Button(text="No, don't cancel.", size=(250, 120), background_color=(.25, 150, .04, 0.5))
        box.add_widget(warning)
        box.add_widget(padding)
        buttons.add_widget(yes_button)
        buttons.add_widget(no_button)
        box.add_widget(buttons)

        pop = Popup(title="Do you wish to cancel?", content= box, size_hint=(None, None), size= (800, 500))
        pop.open()


class CarListButton(ListItemButton):
    pass


class ResultScreen(Screen, BoxLayout):

    car_list = ObjectProperty()

    def build(self):
        header = BoxLayout(orientation="vertical")

        image = Button(text="Image", size=(100, 100), background_color=(0,0,100,1))
        header.add_widget(image)

        return header


    def add_car(self):
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
    Window.size = (850, 1000)
    MainApp().run()




