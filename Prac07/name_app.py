"""Dynamic Names App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicNamesApp(App):
    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Names"
        self.root = Builder.load_file('names_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries.add_widget(temp_label)


DynamicNamesApp().run()
