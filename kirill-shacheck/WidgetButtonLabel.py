import sys
from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit,
    QVBoxLayout, QComboBox, QMainWindow
)

class WidgetStyle(ABC):

    @abstractmethod
    def apply(style, widget):
        pass
    
class DarkStyle(WidgetStyle):
    def apply(self, widget):
        widget.setStyleSheet(
        "background-color: #333333; color: white; padding: 8px;"
    )
    
class LightStyle(WidgetStyle):
    def apply(self, widget):
        widget.setStyleSheet(
        "background-color: white; color: black; padding: 8px;"
    )
    
class GreenStyle(WidgetStyle):
    def apply(self, widget):
        widget.setStyleSheet(
        "background-color: #228B22; color: white; padding: 8px;"
    )
    
    
class WidgetCreator:
    def __init__(self, style):
        self.style = style

    @abstractmethod
    def creator(self, text):
        pass

class ButtonCreator(WidgetCreator):
    def create(self, text):
        widget = QPushButton(text)
        self.style.apply(widget)
        return widget
    
class LabelCreator(WidgetCreator):
    def create(self, text):
        widget = QLabel(text)
        self.style.apply(widget)
        return widget
    
class LineEditCreator(WidgetCreator):
    def create(self, text):
        widget = QLineEdit(text)
        self.style.apply(widget)
        return widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bridge Pattern - Widget Creator")
        self.setMinimumSize(400, 450)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.widget_combo = QComboBox()
        self.widget_combo.addItems([
            "Button", "Label", "LineEdit"
        ])

        self.style_combo = QComboBox()
        self.style_combo.addItems([
            "Dark", "Light", "Green"
        ])

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Введите текст")

        self.create_button = QPushButton("Создать виджет")
        self.create_button.clicked.connect(self.create_widget)

        self.preview_layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите виджет:"))
        layout.addWidget(self.widget_combo)
        layout.addWidget(QLabel("Выберите стиль:"))
        layout.addWidget(self.style_combo)
        layout.addWidget(QLabel("Введите текст:"))
        layout.addWidget(self.text_input)
        layout.addWidget(self.create_button)
        layout.addWidget(QLabel("Предпросмотр:"))
        layout.addLayout(self.preview_layout)
        
    def create_widget(self):
        text = self.text_input.text()
        styles = {
            "Dark": DarkStyle,
            "Light": LightStyle,
            "Green": GreenStyle
        }

        style = styles[self.style_combo.currentText()]()

        creators = {

            "Button": ButtonCreator,
            "Label": LabelCreator,
            "LineEdit": LineEditCreator
        }

        creator_class = creators[self.widget_combo.currentText()]
        creator = creator_class(style)

        widget = creator.create(text)

        self.preview_layout.addWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

