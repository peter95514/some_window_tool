from abc import abstractmethod
from PyQt6.QtWidgets import QMainWindow, QWidget

class Basewidget(QWidget):
    def __init__(self, parent: QMainWindow):
        super().__init__()
        self.setParent(parent)
        self.widget = None

    @abstractmethod
    def create_widget(self):
        pass

class WidgetManager:

    def __init__(self, main_window):
        self.widgets = {}
        self.main_window = main_window

    def add_widget(self, name, widget: Basewidget):
        self.widgets[name] = widget

    def get_widget(self, name):
        return self.widgets[name]
