# Imports
import kivy
from kivy.app import App    # Imports functions to build the app
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from Copart import copart_Scraping
from IAAI import iaai_Scraping
import webbrowser
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.progressbar import ProgressBar
import threading
import time
from kivy.clock import Clock

kivy.require('1.10.1')


def function1():
    Clock.schedule_once(App.get_running_app().show_main_screen)


class MainScreen(Screen, FloatLayout):  # Main Screen Class that holds every method in the Start Screen

    auction_name = " "
    default = "Select an auction"
    selected_auction = StringProperty('Select an auction')
    x_value = 450
    y_value = 500

    def change_label(self, change):  # Changes the text that shows what auction is selected

        strtst = "Selected: " + change

        if self.selected_auction == self.default and (change == "Copart" or change == "IAAI"):
            self.selected_auction = "Selected: " + change
            self.selected_auction = "Selected: " + change
        elif self.selected_auction == strtst or self.selected_auction == "Main":
            self.selected_auction = self.default
        elif change != self.selected_auction:
            if self.selected_auction == "Selected: Copart and IAAI":
                self.selected_auction = "Selected: " + change
            else:
                if change == "None":
                    self.selected_auction == "TO START, PLEASE SELECT AN AUCTION"
                else:
                    self.selected_auction = "Selected: Copart and IAAI"

    def change_screen(self):
        self.manager.current = "Loading Screen"

    t2 = threading.Thread(target=iaai_Scraping.outer)
    t3 = threading.Thread(target=copart_Scraping.run)

    def start_process(self):  # Used to start the web scraping
        if self.selected_auction == 'Selected: Copart':
            self.manager.current = "Loading Screen"
            self.t3.start()
            print("Done it")
            Clock.schedule_once(App.get_running_app().show_main_screen)
            self.selected_auction = "Select an auction"
        elif self.selected_auction == 'Selected: IAAI':
            self.manager.current = "Loading Screen"
            self.t2.start()
            self.selected_auction = "Select an auction"
        elif self.selected_auction == 'Selected: Copart and IAAI':
            self.manager.current = "Loading Screen"
            self.t2.start()
            self.t3.start()
        else:
            self.change_label("None")

        # self.manager.current = "Results Screen"


class LoadingScreen(Screen):

    def cancel(self):
        box = BoxLayout(orientation='vertical')
        padding = Label(text= "If you say yes all progress will be lost!")
        buttons = BoxLayout()
        warning = Image(source="Data/warning.png")
        yes_button = Button(text= "Yes, do cancel it.", on_release=lambda x:self.back(),
                            on_press=lambda *args: pop.dismiss(), size=(250, 120), background_color=(300, 0.5, 0, .7))
        no_button = Button(text="No, don't cancel.", on_press=lambda *args: pop.dismiss(), size=(250, 120),
                           background_color=(.25, 150, .04, 0.5))
        box.add_widget(warning)
        box.add_widget(padding)
        buttons.add_widget(yes_button)
        buttons.add_widget(no_button)
        box.add_widget(buttons)

        pop = Popup(title="Do you wish to cancel?", content=box, size_hint=(None, None), size= (800, 500))
        pop.open()

    def back(self):
        self.manager.current = "Main Screen"
        MainScreen.selected_auction = MainScreen.default

    def test_continue(self):
        self.manager.current = "Results Screen"
        s2 = self.manager.get_screen('Results Screen')
        s2.start()


class ResultScreen(Screen, BoxLayout):

    retrain_list = []

    car_list = ObjectProperty(None)
    source_image_list = ['Data/file01.png', 'Data/file03.png']

    info = []

    i = 0
    source_image = None
    source_makemod = StringProperty("")
    source_extra = StringProperty("")
    index_like = 0
    source_like = 'Data/like_inactive.png'

    def start(self):
        print(len(iaai_Scraping.qualifying_cars_list))

        self.info = [[] for i in range(0, len(iaai_Scraping.qualifying_cars_list))]
        for i in range(0, len(iaai_Scraping.qualifying_cars_list)):
            self.info[i] = iaai_Scraping.qualifying_cars_list[i]
            print(str(self.info[i].specific_url))

        print(self.i)
        self.ids['result_image'].source = self.info[self.i].filename
        self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
        self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
        self.source_like = 'Data/like_inactive.png'

    def hyperlink(self):
        webbrowser.open(self.info[self.i].url)

    def change_like_button(self):
        if self.index_like == 0:
            self.ids['like_button_image'].source = 'Data/like_active.png'
            self.info[self.i].liked = True
            self.index_like = 1
            print(self.info[self.i].liked)
        elif self.index_like == 1:
            self.ids['like_button_image'].source = 'Data/like_inactive.png'
            self.info[self.i].liked = False
            self.index_like = 0

    def increase(self):
        self.i += 1
        if self.i < len(self.info):
            self.ids['result_image'].source = self.info[self.i].filename
            self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
            self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
            if self.info[self.i].liked:
                self.ids['like_button_image'].source = 'Data/like_active.png'
            else:
                self.ids['like_button_image'].source = 'Data/like_inactive.png'
        else:
            self.i -= 1

    def decrease(self):
        self.i -= 1
        if self.i >= 0:
            self.ids['result_image'].source = self.info[self.i].filename
            self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
            print(str(self.ids['result_image'].source))
            self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
            if self.info[self.i].liked:
                self.ids['like_button_image'].source = 'Data/like_active.png'
            else:
                self.ids['like_button_image'].source = 'Data/like_inactive.png'
        else:
            self.i += 1

    def continue_(self):
        self.manager.current = "Retrain Screen"
        self.ids['result_image'].source = self.source_image_list[0]
        # TODO Remove all the elemnts from the source_image_list porque si maje ahuevo


class RetrainingScreen(Screen):
    pass


class Manager(ScreenManager):

    main_screen = ObjectProperty(None)
    loading_screen = ObjectProperty(None)
    results_screen = ObjectProperty(None)


class MainApp(App):

    choice = ""
    source = StringProperty(None)

    def build(self):
        self.m = Manager(transition=NoTransition())
        return self.m

    def show_main_screen(self, dt):
        self.m.current = "Results Screen"


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (850, 1000)
    MainApp().run()
