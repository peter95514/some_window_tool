from abc import abstractmethod
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import QPoint, Qt
import os
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Basewidget(QWidget):
    def __init__(self, parent: QMainWindow, manager : "WidgetManager", movable = True, name = None):
        super().__init__()
        self.setParent(parent)
        self.widget = None
        self.movable = movable
        self.name = name
        self.manager = manager 
        self.manager.restore_widget(self.name, self)

    @abstractmethod
    def create_widget(self):
        pass

    def mousePressEvent(self, event):
        if not self.movable:
            return super().mousePressEvent(event)  # 不可拖動就呼叫原本事件
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if not self.movable:
            return super().mouseMoveEvent(event)
        if self.dragging:
            new_pos = event.globalPosition().toPoint() - self.drag_offset
            self.move(new_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if not self.movable:
            return super().mouseReleaseEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()

        self.manager.record_widget(self.name, self)


class WidgetManager:

    def __init__(self, main_window):
        self.widgets = {}
        self.main_window = main_window
        self.json_path = os.path.join(root_path, "data/config/widget_state.json")
        self.state = self.load_state()

    def load_state(self):
        if not os.path.exists(self.json_path):
            with open(self.json_path, "w") as f:
                json.dump({}, f)

        if os.path.exists(self.json_path):
            with open(self.json_path, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_state(self):
        with open(self.json_path, "w") as f:
            json.dump(self.state, f, indent=4)
    
    def record_widget(self, name, widget: QWidget):
        self.state[name] = {
            "x" : widget.x(),
            "y" : widget.y()
        }
        self.save_state()

    def restore_widget(self, name, widget: QWidget):
        state_widget = self.state.get(name)
        if not state_widget:
            return
        print("move success")
        geom = widget.geometry()
        widget.setGeometry(state_widget["x"], state_widget["y"], geom.width(), geom.height())
        widget.move(state_widget["x"], state_widget["y"])

    def add_widget(self, name, widget: Basewidget):
        self.widgets[name] = widget

    def get_widget(self, name):
        return self.widgets[name]
