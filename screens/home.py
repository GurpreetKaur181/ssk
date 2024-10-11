from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ImageSlider())

class ImageSlider(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 0 
        self.spacing = 0  

        # Image widget with responsive height
        self.image = Image(source='images/ssk1.png', 
                           allow_stretch=True, 
                           keep_ratio=True,  # Maintain aspect ratio
                           size_hint=(1, 0.7))  # 70% height for image
        self.add_widget(self.image)

        # BoxLayout for boxes below the image
        boxes_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3))  # 30% height for boxes

        # Create 3 boxes (buttons in this case)
        for i in range(3):
            box = Button(text=f'Box {i + 1}', size_hint=(1, None), height='48dp')  # Use dp for consistent button height
            boxes_layout.add_widget(box)

        self.add_widget(boxes_layout)

        # Start automatic image change
        Clock.schedule_interval(self.auto_change_image, 2)  # Change every 2 seconds
        self.current_image_index = 0

    def update_image_and_label(self):
        # List of image sources
        image_files = [f'images/ssk{i + 1}.png' for i in range(9)]
        
        if 0 <= self.current_image_index < len(image_files):
            self.image.source = image_files[self.current_image_index]
            self.image.reload()  # Reload the image to reflect the change

    def auto_change_image(self, dt):
        self.current_image_index = (self.current_image_index + 1) % 5  # Loop through 9 images
        self.update_image_and_label()
