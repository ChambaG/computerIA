# Imports
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
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
import time


kivy.require('1.10.1')


def change(self, screen):
    self.manager.current = screen


class MainScreen(Screen, FloatLayout):  # Main Screen Class that holds every method in the Start Screen

    auction_name = " "
    selected_auction = StringProperty('Select an auction')
    x_value = 450
    y_value = 500

    def start_process(self):  # Used to start the web scraping
        if self.selected_auction == 'Selected: Copart':
            main.run()
        elif self.selected_auction == 'Selected: IAAI':
            self.manager.current = "Loading Screen"
            iaai_Scraping.initiate()
        elif self.selected_auction == 'Selected: Copart and IAAI':
            LoadingScreen.pleasework(self)
        """else:
            self.manager.current = "Loading Screen"""""

    def change_label(self, change):  # Changes the text that shows what auction is selected
        if self.selected_auction == 'Selected: Copart' or self.selected_auction == 'Selected: IAAI':
            self.selected_auction = 'Selected: Copart and IAAI'
        else:
            self.selected_auction = 'Selected: {}'.format(change)
        print(self.selected_auction)


    def change_Screen(self):
        self.manager.current = "Loading Screen"


class LoadingScreen(Screen):

    def pleasework(self):
        main.run()

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

    def test_continue(self):
        self.manager.current = "Results Screen"


class CarListButton(ListItemButton):
    pass


class ResultScreen(Screen, BoxLayout):

    car_list = ObjectProperty()
    image_to_display = "Data/test.png"

    def continue_(self):
        self.manager.current = "Retrain Screen"
        RetrainingScreen.loading(self)


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

    def build(self):
        m = Manager(transition=NoTransition())
        return m


if __name__ == "__main__":
    Window.clearcolor = (.46875, .46875, .4765, 1)
    Window.size = (850, 1000)
    MainApp().run()
