from frontend.widgets import widget_manager 
from PyQt6 import QtWidgets, QtCore



class clock(widget_manager.Basewidget):
    def __init__(self, parent: QtWidgets.QMainWindow, pos):

        super().__init__(parent)
        self.pos = pos
        self.setFixedSize(900, 900)
        self.create_widget()

        #self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        #self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.move(*pos)
        
    def create_widget(self):
       layout = QtWidgets.QVBoxLayout()
       self.setLayout(layout)
       label = QtWidgets.QLabel("test")
       label.setStyleSheet("color: red; font-size: 20px")
       label.resize(500,500)
       layout.addWidget(label)

