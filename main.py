
from kivy.app import App
from frontend.frontend import CameraInterface


class CameraApp(App):
    def build(self):
        return CameraInterface()


if __name__ == "__main__":
    CameraApp().run()
