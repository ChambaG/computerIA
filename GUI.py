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
import threading
from kivy.clock import Clock
import time

kivy.require('1.10.1')


def iaai():
    iaai_Scraping.testing()
    Clock.schedule_once(App.get_running_app().show_results)


def retrain():
    time.sleep(10)
    Clock.schedule_once(App.get_running_app().show_results)


def copart():
    copart_Scraping.run()
    Clock.schedule_once(App.get_running_app().show_results)


class MainScreen(Screen, FloatLayout):  # Main Screen Class that holds every method in the Start Screen

    auction_name = " "
    default = "Select an Auction"
    selected_auction = StringProperty("")
    x_value = 450
    y_value = 500
    error = "TO START, PLEASE SELECT AN AUCTION"

    def start(self):
        self.auction_name = ""
        self.selected_auction = 'Select an Auction'

    def change_label(self, change):  # Changes the text that shows what auction is selected

        strtst = "Selected: " + change

        if (self.selected_auction == self.default or self.selected_auction == self.error) and (change == "Copart" or change == "IAAI"):
            print("First")
            self.selected_auction = "Selected: " + change
        elif self.selected_auction == strtst:
            self.selected_auction = self.default
        elif change != self.selected_auction:
            if self.selected_auction == "Selected: Copart and IAAI":
                self.selected_auction = "Selected: " + change
            else:
                if change == "None":
                    print("here 1")
                    self.selected_auction = "TO START, PLEASE SELECT AN AUCTION"

    def change_screen(self):
        self.manager.current = "Loading Screen"

    t1 = threading.Thread(target=iaai)
    t2 = threading.Thread(target=copart)

    def start_process(self):  # Used to start the web scraping
        print(self.selected_auction)
        if self.selected_auction == 'Selected: Copart':
            self.manager.current = "Loading Screen"
            self.t2.start()
        elif self.selected_auction == 'Selected: IAAI':
            self.manager.current = "Loading Screen"
            self.t1.start()
        elif self.selected_auction == 'Selected: Copart and IAAI':
            self.manager.current = "Loading Screen"
            self.t1.start()
            self.t2.start()
        else:
            print("Nothing")
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
            command = self.manager.get_screen('Retrain Screen')
            command.start()


class RetrainingScreen(Screen):

        t1 = threading.Thread(target=retrain)

        def start(self):
            self.manager.current = "Retrain Screen"
            self.t1.start()


class Manager(ScreenManager):

    main_screen = ObjectProperty(None)
    loading_screen = ObjectProperty(None)
    results_screen = ObjectProperty(None)
    retraining_screen = ObjectProperty(None)


class MainApp(App):

    choice = ""
    source = StringProperty(None)

    def build(self):
        self.m = Manager(transition=NoTransition())
        s2 = self.m.get_screen('Main Screen')
        s2.start()
        return self.m

    def show_results(self, dt):
        self.m.current = "Results Screen"
        s2 = self.m.get_screen('Results Screen')
        s2.start()


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (850, 1000)
    MainApp().run()
