from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image  # Use standard Image instead

class GuestTalkScreen(Screen):
    def __init__(self, **kwargs):
        super(GuestTalkScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', padding=10)

        # Use the standard Image widget
        image = Image(source='images/Logo.jpg', allow_stretch=True, size_hint=(1, None), height='200dp')

        # Add the first label
        title_label = MDLabel(
            text='Academics Guest Talk',
            halign='center',
            size_hint_y=None,
            height='50dp'
        )

        # Add the second label
        details_label = MDLabel(
            text='Details about the guest talk will go here.',
            halign='center',
            size_hint_y=None,
            height='50dp'
        )

        layout.add_widget(image)
        layout.add_widget(title_label)
        layout.add_widget(details_label)
        self.add_widget(layout)
