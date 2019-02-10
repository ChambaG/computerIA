# Imports
import kivy
from kivy.app import App    # Imports functions to build the app
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from Copart import copart_Scraping
from IAAI import iaai_Scraping
from kivy.uix.widget import Widget
from kivy.clock import Clock
from functools import partial
import time


kivy.require('1.10.1')


def change(self, screen):
    self.manager.current = screen


class MainScreen(Screen, FloatLayout):  # Main Screen Class that holds every method in the Start Screen

    auction_name = " "
    default = "Select an auction"
    selected_auction = StringProperty('Select an auction')
    x_value = 450
    y_value = 500

    def start_process(self, change):  # Used to start the web scraping
        print("Pressed start")
        self.manager.current = "Loading Screen"
        if self.selected_auction == 'Selected: Copart':
            self.manager.current = "Loading Screen"
            self.run(1)
            print("Running")
            self.selected_auction = "Select an auction"
        elif self.selected_auction == 'Selected: IAAI':
            self.manager.current = "Loading Screen"
            iaai_Scraping.initiate()
            self.selected_auction = "Select an auction"
        elif self.selected_auction == 'Selected: Copart and IAAI':
            LoadingScreen.pleasework(self)
        else:
            self.change_label("None")

    def change_label(self, change):  # Changes the text that shows what auction is selected

        strtst = "Selected: " + change
        print(change)

        if self.selected_auction == self.default and (change == "Copart" or change == "IAAI"):
            self.selected_auction = "Selected: " + change
            print(self.selected_auction + str(1))
            self.selected_auction = "Selected: " + change
        elif self.selected_auction == strtst or self.selected_auction == "Main":
            self.selected_auction = self.default
            print(self.selected_auction + str(2))
        elif change != self.selected_auction:
            if self.selected_auction == "Selected: Copart and IAAI":
                print("entered")
                print(change)
                self.selected_auction = "Selected: " + change
            else:
                if change == "None":
                    print("yes")
                    self.selected_auction == "TO START, PLEASE SELECT AN AUCTION"
                    print("executed")
                else:
                    self.selected_auction = "Selected: Copart and IAAI"

            print(self.selected_auction + " end")

    def change_screen(self):
        self.manager.current = "Loading Screen"

    def run(self, code):
        if code == 1:
            copart_Scraping.run()
        elif code == 2:
            iaai_Scraping.initiate()
        else:
            copart_Scraping.run()
            iaai_Scraping.initiate()


class LoadingScreen(Screen):

    def pleasework(self):
        copart_Scraping.run()

    def cancel(self):
        box = BoxLayout(orientation='vertical')
        padding = Label(text= "If you say yes all progress will be lost!")
        buttons = BoxLayout()
        warning = Image(source="Data/warning.png")
        yes_button = Button(text= "Yes, do cancel it.", on_release=lambda x:self.back(), on_press=lambda *args: pop.dismiss(),
                            size=(250, 120), background_color=(300, 0.5, 0, .7))
        no_button = Button(text="No, don't cancel.", on_press=lambda *args: pop.dismiss(), size=(250, 120),
                           background_color=(.25, 150, .04, 0.5))
        box.add_widget(warning)
        box.add_widget(padding)
        buttons.add_widget(yes_button)
        buttons.add_widget(no_button)
        box.add_widget(buttons)

        pop = Popup(title="Do you wish to cancel?", content= box, size_hint=(None, None), size= (800, 500))
        pop.open()

    def back(self):
        self.manager.current = "Main Screen"
        MainScreen.selected_auction = MainScreen.default

    def test_continue(self):
        self.manager.current = "Results Screen"


class CarListButton(ListItemButton):
    pass


class ResultScreen(Screen, BoxLayout):

    car_list = ObjectProperty(None)
    source_image_list = ['Data/file01.png', 'Data/file02.png', 'Data/file03.png']
    information_list = []
    i = 0
    source_image = source_image_list[i]

    def increase(self):
        self.i += 1
        if self.i < len(self.source_image_list):
            self.ids['result_image'].source = self.source_image_list[self.i]
            print(self.ids['result_image'].source)
        else:
            self.i -= 1

    def decrease(self):
        self.i -= 1
        if self.i >= 0:
            self.ids['result_image'].source = self.source_image_list[self.i]
            print(self.ids['result_image'].source)
        else:
            self.i += 1

    def continue_(self):
        self.manager.current = "Retrain Screen"
        RetrainingScreen.loading(self)
        self.ids['result_image'].source = self.source_image_list[0]
        # TODO Remove all the elemnts from the source_image_list porque si maje ahuevo

    def add_car(self):
        pass


class RetrainingScreen(Screen):

    def loading(self):
        self.manager.current = "Main Screen"


class Manager(ScreenManager):

    main_screen = ObjectProperty(None)
    loading_screen = ObjectProperty(None)
    results_screen = ObjectProperty(None)


class MainApp(App):

    choice = ""
    source = StringProperty(None)

    def build(self):
        m = Manager(transition=NoTransition())
        return m


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (850, 1000)
    MainApp().run()
