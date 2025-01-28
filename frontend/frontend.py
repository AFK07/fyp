# frontend/frontend.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from backend.backend import CameraBackend


class CameraInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Add Camera widget
        self.camera = Camera(play=True)  # 'play=True' starts the camera
        self.add_widget(self.camera)

        # Add a button to capture an image
        capture_button = Button(text="Capture Photo", size_hint=(1, 0.1))
        capture_button.bind(on_press=self.capture_image)
        self.add_widget(capture_button)

    def capture_image(self, instance):
        """
        Capture the image using the backend logic.
        """
        CameraBackend.save_image(self.camera)
