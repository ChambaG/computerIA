from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.graphics import Color


gui = '''
<MenuScreen>:
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            texture: self.background_image.texture
            pos: self.pos
            size: self.size
    GridLayout:
        size_hint: .1, .1
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows: 1
        Button:
            text: 'Play'
            font_size: 20
            font_name: 'DroidSans'
            bold: True
            italic: True
            height: 10
            background_color: (0.5, 0.7, 0.5, 0.9)
            #Read more about them from documentation
            background_normal: './images/orange.png'
            background_down: './images/green.png'
            border: 30,30,30,30
            color: (1, .3, .8, .5)
            on_press: self.text = 'Oh yeah'

'''


class MenuScreen(Screen):
    background_image = ObjectProperty(
                                Image(
                                    source='../Examples/examples/widgets/sequenced_images/data/images/button_white_animated.zip',
                                    anim_delay=.5))
    Builder.load_string(gui)
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))


class MyJB(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MyJB().run()
