# backend/backend.py

class CameraBackend:
    @staticmethod
    def save_image(camera):
        """
        Save the current frame from the camera.
        :param camera: The Kivy Camera widget instance.
        """
        if camera.texture:
            camera.export_to_png("captured_image.png")
            print("Image saved as 'captured_image.png'")
        else:
            print("No texture available from the camera.")
