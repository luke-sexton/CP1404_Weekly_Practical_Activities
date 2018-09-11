from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKilometresConverter(App):
    """MilesToKilometresConverter is a Kivy App that converts user input of miles into kilometres."""
    def build(self):
        """Build the Kivy app from .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("miles_to_kilometres.kv")
        return self.root

    def handle_calculate(self):
        """Handles calculation from miles to kilometres"""
        value = self.valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_up_or_down(self, up_or_down):
        """Handles and updates user input when up or down is pressed."""
        value = self.valid_miles() + up_or_down
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def valid_miles(self):
        """Validates user input - Converts to float, return 0 if error."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometresConverter().run()
