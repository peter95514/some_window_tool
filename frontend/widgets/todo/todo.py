from PyQt6.QtWidgets import QMainWindow, QWidget
from frontend.widgets import widget_manager
from frontend.widgets.widget_manager import WidgetManager, Basewidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class todo_widget(Basewidget):

    def __init__(self, parent: QMainWindow, manager:"WidgetManager"):
        super().__init__(parent, manager, True, "todo_widget")
        self.size_of_screen = (400,600)
        self.setFixedSize(*self.size_of_screen)


    


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

