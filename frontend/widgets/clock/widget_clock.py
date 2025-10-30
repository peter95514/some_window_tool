from frontend.widgets import widget_manager 
from PyQt6 import QtWidgets, QtCore



class clock(widget_manager.Basewidget):

    def __init__(self, parent: QtWidgets.QMainWindow, pos, manager):

        super().__init__(parent,manager, True, "clock")
        self.size_of_screen = (300, 300)
        self.setFixedSize(*self.size_of_screen)
        self.create_widget()
        self.setStyleSheet("""
            background-color: rgba(50, 50, 50, 180);
            border-radius: 10px;
        """)

        #self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        #self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        #self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
    def create_widget(self):
       layout = QtWidgets.QVBoxLayout()
       self.setLayout(layout)
       label = QtWidgets.QLabel("test")
       label.setStyleSheet("color: red; font-size: 20px")
       label.resize(500,500)
       layout.addWidget(label)

