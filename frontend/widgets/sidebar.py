from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(300)
        self.setFixedHeight(parent.height())
        self.setStyleSheet("background-color: rgba(30, 30, 30, 200); border-radius: 8px;")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("📋 ToDo Widget Placeholder"))
        layout.addWidget(QLabel("☁️ Weather Widget Placeholder"))
        layout.addStretch()
        self.setLayout(layout)

