from PyQt6 import QtWidgets
from frontend.widgets import widget_manager
from PyQt6.QtCore import Qt, QPropertyAnimation
from PyQt6.QtGui import QPainter, QColor
from .. import widget_manager

class sidebar(widget_manager.Basewidget):

    def __init__(self, parent: QtWidgets.QMainWindow, manager:"widget_manager.WidgetManager"):
        super().__init__(parent, manager, False, "sidebar")
        self.widget_size = self.manager.get_screen_size()
        self.widget_size = ((int)(self.widget_size[0] * 0.2), (int)(self.widget_size[1] * 0.7))
        self.setFixedSize(*self.widget_size)
        self.setGeometry(self.manager.get_screen_size()[0] - self.widget_size[0], (int)(self.manager.get_screen_size()[1] * 0.3 - 45), self.widget_size[0], self.widget_size[1])

        self.create_widget()
        self.manager.record_widget("sidebar", self)

        self.hidepos = self.x() + self.width() + 10
        self.showpos = self.x()

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(Qt.EasingCurve.OutCubic)

    def create_widget(self):
        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
            }
            QCalendarWidget QToolButton {
                color: black;
                background-color: lightgray;
                border-radius: 5px;
                padding: 3px;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: black;
                selection-background-color: #3daee9;
                selection-color: white;
            }
        """)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        
        layout.addWidget(self.calendar)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

