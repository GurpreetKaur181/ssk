# screens/about.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Image(source='images/Logo.png', allow_stretch=True, size_hint=(1, 1)))
        layout.add_widget(Label(text='About Screen', halign='center', size_hint_y=None, height=50))
        self.add_widget(layout)
