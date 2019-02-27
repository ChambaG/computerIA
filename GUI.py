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
from kivy.clock import Clock
import copart_Scraping
import iaai_Scraping
import webbrowser
import threading
import nn
import time
import os.path


# These functions are used to set the target tasks for the threads
def iaai():  # Function that starts the web scraping for IAAI
    iaai_Scraping.initiate()  # Line accessing and running initiate() from iaai_Scraping.py class
    print("IAAI IS DONE")
    Clock.schedule_once(App.get_running_app().show_results)  # Runs the show_results() function in the MainApp class


def retrain(inputs):  # Function that sends the liked cars to the neural network so that it retrains
    #nn.retrain(inputs)
    time.sleep(120)
    Clock.schedule_once(App.get_running_app().done) # Runs the done() function in the MainApp class


def copart():  # Function that starts the web scraping for Copart
    copart_Scraping.run()
    print("COPART IS DONE")
    Clock.schedule_once(App.get_running_app().show_results)  # Runs the show_results() function in the MainApp class


def both():  # Function that starts the web scraping for both auctions
    copart_Scraping.run()
    iaai_Scraping.initiate()
    Clock.schedule_once(App.get_running_app().show_results)  # Runs the show_results() function in the MainApp class


kivy.require('1.10.1')


class MainScreen(Screen, FloatLayout):  # Main Screen Class that holds every method in the Start Screen

    auction_name = " "
    default = "Select an Auction"
    selected_auction = StringProperty("")  # This is the string that holds the user feedback in the main screen
    x_value = 450
    y_value = 500
    error = "TO START, PLEASE SELECT AN AUCTION"

    def start(self):
        self.auction_name = ""
        self.selected_auction = 'Select an Auction'

    def change_label(self, change):  # Changes the text that shows what auction is selected

        strtst = "Selected: " + change
        print(change)

        if (self.selected_auction == self.default or self.selected_auction == self.error) and (change == "Copart" or change == "IAAI"):
            self.selected_auction = "Selected: " + change
        elif self.selected_auction == strtst:
            self.selected_auction = self.default
        elif strtst != self.selected_auction:
            if self.selected_auction == "Selected: Copart and IAAI":
                self.selected_auction = "Selected: " + change
            else:
                if change == "None":
                    self.selected_auction = "TO START, PLEASE SELECT AN AUCTION"
                else:
                    self.selected_auction = "Selected: Copart and IAAI"

    #
    def change_screen(self):
        self.manager.current = "Loading Screen"

    t1 = threading.Thread(target=iaai)  # Creates a thread and sets its target to function iaai() in the outer scope
    t2 = threading.Thread(target=copart)  # Creates a thread and sets its target to function copart() in the outer scope
    t3 = threading.Thread(target=both)

    def start_process(self):  # Used to start the web scraping. Each thread is started according to the specified
        # auctions the user wants to be scraped
        if self.selected_auction == 'Selected: Copart':
            self.manager.current = "Loading Screen"
            self.t2.start()
        elif self.selected_auction == 'Selected: IAAI':
            self.manager.current = "Loading Screen"
            self.t1.start()
        elif self.selected_auction == 'Selected: Copart and IAAI':
            self.manager.current = "Loading Screen"
            self.t3.start()
        else:
            self.change_label("None")


class LoadingScreen(Screen):

    def cancel(self):
        box = BoxLayout(orientation='vertical')
        padding = Label(text= "If you say yes all progress will be lost!")
        buttons = BoxLayout()
        warning = Image(source="/Users/salvag/Documents/GitHub/computerIA/Data/warning.png")
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


class ResultScreen(Screen, FloatLayout):

    retrain_list = []

    car_list = ObjectProperty(None)

    info = []

    i = 0
    source_image = None
    source_makemod = StringProperty("")
    source_extra = StringProperty("")
    index_like = 0
    source_like = '/Users/salvag/Documents/GitHub/computerIA/Data/like_inactive.png'

    def start(self):
        print("Length of info: " + str(len(self.info)))
        for i in range(0, len(iaai_Scraping.qualifying_cars_list)):
            self.info.append(iaai_Scraping.qualifying_cars_list[i])

        print("Length of info after iaai: " + str(len(self.info)))

        for i in range(0, len(copart_Scraping.qualifying_cars_list)):
            self.info.append(copart_Scraping.qualifying_cars_list[i])

        print("Length of info after copart: " + str(len(self.info)))

        self.ids['result_image'].source = self.info[self.i].filename
        self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
        self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
        self.source_like = '/Users/salvag/Documents/GitHub/computerIA/Data/like_inactive.png.png'

    def hyperlink(self):
        webbrowser.open(self.info[self.i].url)

    def change_like_button(self):
        if self.index_like == 0:
            self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_active.png'
            self.info[self.i].liked = True
            self.index_like = 1
        elif self.index_like == 1:
            self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_inactive.png.png'
            self.info[self.i].liked = False
            self.index_like = 0

    def increase(self):
        self.i += 1
        if self.i < len(self.info):
            self.ids['result_image'].source = self.info[self.i].filename
            self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
            self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
            if self.info[self.i].liked:
                self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_active.png'
            else:
                self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_inactive.png.png'
        else:
            self.i -= 1

    def decrease(self):
        self.i -= 1
        if self.i >= 0:
            self.ids['result_image'].source = self.info[self.i].filename
            self.source_makemod = str(self.info[self.i].year) + " " + self.info[self.i].make + " " + self.info[self.i].model
            self.source_extra = self.info[self.i].damage + " | $" + self.info[self.i].bid
            if self.info[self.i].liked:
                self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_active.png'
            else:
                self.ids['like_button_image'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/like_inactive.png.png'
        else:
            self.i += 1

    def continue_(self):
        for i in range(0, len(self.info)):
            if self.info.liked:
                self.retrain_list.append(self.info[i].input)

        command = self.manager.get_screen('Retrain Screen')
        command.start()


class RetrainingScreen(Screen):

    d1 = threading.Thread(target=retrain)

    def start(self):
        self.manager.current = "Retrain Screen"
        self.d1.start()

    def change(self):
        self.ids['img_gif'].source = '/Users/salvag/Documents/GitHub/computerIA/Data/done.gif'
        self.ids['img_gif'].anim_delay = 0.045


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

    def done(self, dt):
        self.m.current = "Main Screen"
        mypath = "/Users/salvag/Documents/GitHub/computerIA/Images"  # Enter your path here
        for root, dirs, files in os.walk(mypath):
            for file in files:
                os.remove(os.path.join(root, file))

    def show_results(self, dt):
        self.m.current = "Results Screen"
        s2 = self.m.get_screen('Results Screen')  # Stores the Results Screen widget as s2
        s2.start()  # Runs the function start() in the ResultScreen class


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (850, 1000)
    MainApp().run()
