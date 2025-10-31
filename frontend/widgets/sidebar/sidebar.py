from PyQt6 import QtWidgets
from frontend.widgets import widget_manager
from PyQt6.QtCore import QTimer, Qt, QTime, QDate
from PyQt6.QtGui import QPainter, QColor

class sidebar(widget_manager.Basewidget):

    def __init__(self, parent: QtWidgets.QMainWindow, manager):
        super().__init__(parent, manager, True, "sidebar")
        self.setStyleSheet("""
            background-color: rgba(50, 50, 50, 180);
            border-radius: 10px;
        """)
        self.create_widget()
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

    def resizeEvent(self, event):
        parent = self.parentWidget()
        print(parent)
        if parent:
            pw = parent.width()
            ph = parent.height()
            print(pw, " ", ph)
            w = (int)(pw * 0.3)
            self.setGeometry(pw - w, 0, w, ph)
