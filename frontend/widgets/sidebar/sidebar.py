from PyQt6 import QtWidgets
from frontend.widgets import widget_manager
from PyQt6.QtCore import QTimer, Qt, QTime, QDate
from PyQt6.QtGui import QPainter, QColor
from .. import widget_manager

class sidebar(widget_manager.Basewidget):

    def __init__(self, parent: QtWidgets.QMainWindow, manager:"widget_manager.WidgetManager"):
        super().__init__(parent, manager, False, "sidebar")
        self.widget_size = self.manager.get_screen_size()
        self.widget_size = ((int)(self.widget_size[0] * 0.2), (int)(self.widget_size[1] * 0.7))
        self.setFixedSize(*self.widget_size)
        self.setGeometry(self.manager.get_screen_size()[0] - self.widget_size[0], (int)(self.manager.get_screen_size()[1] * 0.3 - 45), self.widget_size[0], self.widget_size[1])
        print(self.x(), self.y())

        self.setStyleSheet("""
            background-color: rgba(100, 50, 50, 0);
            border-radius: 10px;
        """)
        self.create_widget()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

