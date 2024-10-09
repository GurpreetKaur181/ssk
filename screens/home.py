from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ImageSlider())

class ImageSlider(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Image widget
        self.image = Image(source='images/ssk1.png', size_hint=(1, 10))
        self.add_widget(self.image)

        # Slider widget
        self.slider = Slider(min=0, max=4, value=0)  # Change max to 4 for 5 images
        self.slider.bind(value=self.on_slider_value_change)
        self.add_widget(self.slider)

        # Label widget (optional)
        self.label = Label(text='Select an image using the slider', size_hint=(1, 0.2))
        self.add_widget(self.label)

        # Start automatic image change
        Clock.schedule_interval(self.auto_change_image, 2)  # Change every 2 seconds
        self.current_image_index = 0

    def on_slider_value_change(self, slider, value):
        self.current_image_index = int(value)
        self.update_image_and_label()

    def update_image_and_label(self):
        # Update images and labels based on current index
        if self.current_image_index == 0:
            self.image.source = 'images/ssk1.png'
            self.label.text = 'Image 1'
        elif self.current_image_index == 1:
            self.image.source = 'images/ssk2.png'
            self.label.text = 'Image 2'
        elif self.current_image_index == 2:
            self.image.source = 'images/ssk3.png'
            self.label.text = 'Image 3'
        elif self.current_image_index == 3:
            self.image.source = 'images/ssk4.png'
            self.label.text = 'Image 4'
        elif self.current_image_index == 4:
            self.image.source = 'images/ssk5.png'
            self.label.text = 'Image 5'

        self.image.reload()

    def auto_change_image(self, dt):
        self.current_image_index = (self.current_image_index + 1) % 5  # Loop through 5 images
        self.slider.value = self.current_image_index  # Update slider position
        self.update_image_and_label()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    MyApp().run()
