import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from . import widget_manager
from .clock import widget_clock
from .sidebar import sidebar

init_pos = (600,400)

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.manager = widget_manager.WidgetManager(self)

        self.manager.add_widget("clock", widget_clock.clock(self, self.manager))
        self.manager.record_widget("clock", self.manager.get_widget("clock"))

        self.manager.add_widget("sidebar", sidebar.sidebar(self, self.manager))
        self.manager.record_widget("sidebar", self.manager.get_widget("sidebar"))

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        #self.setWindowFlag(QtCore.Qt.WindowType.WindowTransparentForInput)

        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

