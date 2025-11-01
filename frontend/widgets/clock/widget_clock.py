from PyQt6.QtGui import QPainter, QColor
from frontend.widgets import widget_manager 
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QTimer, Qt, QTime, QDate

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class clock(widget_manager.Basewidget):

    def __init__(self, parent: QtWidgets.QMainWindow, manager):

        super().__init__(parent, manager, True, "clock")
        self.size_of_screen = (300, 300)
        self.setFixedSize(*self.size_of_screen)
        self.create_widget()
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    def create_widget(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label.setStyleSheet("""
            background-color: transparent;
            color: white;
            font-size: 36px;
        """)

        self.date_label = QtWidgets.QLabel(self)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_label.setStyleSheet("""
            background-color: transparent;
            font-size: 20px;
            color: white;
        """)

        #self.label.setFixedSize(300,200)
        #self.label.sizePolicy().setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Fixed)
        #self.label.sizePolicy().setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Fixed)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.date_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        today = QDate.currentDate()
        self.label.setText(current_time)
        self.date_label.setText(today.toString("yyyy-MM-dd  ") + weekday[today.dayOfWeek() - 1])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)
