# screens/contact.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=10)

        layout.add_widget(MDLabel(text='Contact Us', halign='center', size_hint_y=None, height='50dp'))

        self.name_field = MDTextField(hint_text='Your Name', size_hint_y=None, height='40dp')
        self.email_field = MDTextField(hint_text='Your Email', size_hint_y=None, height='40dp')

        submit_button = MDRaisedButton(text='Submit', size_hint_y=None, height='50dp')
        submit_button.bind(on_press=self.submit_contact_form)

        layout.add_widget(self.name_field)
        layout.add_widget(self.email_field)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def submit_contact_form(self, instance):
        name = self.name_field.text
        email = self.email_field.text
        
        if name and email:
            print(f"Contact form submitted! Name: {name}, Email: {email}")
        else:
            print("Please fill in all fields.")
