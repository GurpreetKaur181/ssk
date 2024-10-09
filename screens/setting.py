# screens/setting.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical')
        
        label = MDLabel(text='Settings screen', halign='center', size_hint_y=None, height='50dp')
        layout.add_widget(label)
        
        self.add_widget(layout)
