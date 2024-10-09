from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from screens.home import HomeScreen
from screens.about import AboutScreen  
from screens.contact import ContactScreen 
from screens.setting import SettingsScreen
from screens.talk import GuestTalkScreen

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))  
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))  
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GuestTalkScreen(name='guest_talk'))
        
        return Builder.load_string(KV)

    def open_nav_drawer(self):
        self.root.ids.nav_drawer.set_state('open')

KV = '''  
<CustomLabel@Label>:
    canvas.before:
        Ellipse:
            pos: self.x - self.height / 4, self.y - self.height / 4
            size: self.height, self.height

    
MDBoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'My Kivy App'
        left_action_items: [['menu', lambda x: app.open_nav_drawer()]]
        right_action_items: [['bell', lambda x: app.show_notifications()]]
        md_bg_color: 85/255, 0, 170/255, 1

    MDNavigationLayout:
        id: nav_layout

        ScreenManager:
            id: screen_manager

            HomeScreen:
                name: 'home'

            AboutScreen:
                name: 'about'

            ContactScreen:
                name: 'contact'

            SettingsScreen:
                name: 'settings'

            GuestTalkScreen:
                name: 'guest_talk'

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                padding: 0
                spacing: 0

                CustomLabel:
                    text: 'Samanvit Siksha Kendra (SSK)'
                    font_size: '24sp'
                    halign: 'center'
                    size_hint_y: None
                    height: dp(50)
                    valign: 'middle'
                    text_size: self.size
                    color: 0, 0, 0, 1 # Black text color
                    
                Image:
                    source: 'images/Logo.png'
                    size_hint: (1, None)
                    height: dp(200)

                MDList:
                    OneLineIconListItem:
                        text: 'Home'
                        on_press:
                            screen_manager.current = 'home'
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'home'

                    OneLineIconListItem:
                        text: 'About'
                        on_press:
                            screen_manager.current = 'about'
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'information-outline'

                    OneLineIconListItem:
                        text: 'Contact Us'
                        on_press:
                            screen_manager.current = 'contact'
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'mail'

                    OneLineIconListItem:
                        text: 'Settings'
                        on_press:
                            screen_manager.current = 'settings'
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'cog'

                    OneLineIconListItem:
                        text: 'Academics Guest Talk'
                        on_press:
                            screen_manager.current = 'guest_talk'
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'microphone'
'''

if __name__ == '__main__':
    MyApp().run()