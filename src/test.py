from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Threebythreeone(BoxLayout):
    pass


class Noughtsandcrosses(BoxLayout):
    pass

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDTopAppBar"

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    Test().run()

from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Threebythreeone(BoxLayout):
    pass


class Noughtsandcrosses(BoxLayout):
    pass

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDTopAppBar"

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    Test().run()