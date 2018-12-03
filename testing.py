from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout


from kivy.uix.label import Label
from kivy.uix.image import Image


import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.image import Image
from os.path import join




class SMApp(App):

    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)



        for i in range(80):
           la = GridLayout(cols=3, padding=10, spacing=10,
                size_hint=(None, None), width=500)
           btn = Label(text=str(i), size_hint_y=None, pos=(50,-200*i))
           filename = join(kivy.kivy_data_dir, 'logo', 'kivy-icon-256.png')
           l1 = Image(source=filename, size_hint_y=None)#,# pos=(0,-200*i), size=(50,50))
           l3 = Image(source=filename, size_hint_y=None)#, pos=(100,-200*i), size=(50,50))

           l2 = Image(source="las.jpg", size_hint_y=None, pos=(0,-200*i-100),  size=(1200,100))

           la.add_widget(btn)
           la.add_widget(l1)
           la.add_widget(l3)
           layout.add_widget(la)
           la2 = GridLayout(cols=1, padding=10, spacing=10,
                 size_hint=(None, None), width=500)

           la2.add_widget(l2)
           layout.add_widget(la2)
        layout.bind(minimum_height=layout.setter('height'))
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)


        root.add_widget(layout)

        return root

if __name__ == '__main__':
    SMApp().run()