
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout,
    QComboBox, QGroupBox
)


# Абстрактный класс стиля
class WidgetStyle(ABC):

    @abstractmethod
    def apply(self, widget):
        pass


# Темный стиль
class DarkStyle(WidgetStyle):

    def apply(self, widget):
        widget.setStyleSheet("""
            background-color: #333333;
            color: white;
            border: 2px solid #555555;
            padding: 8px;
            border-radius: 5px;
        """)


# Светлый стиль
class LightStyle(WidgetStyle):

    def apply(self, widget):
        widget.setStyleSheet("""
            background-color: #eeeeee;
            color: black;
            border: 2px solid #aaaaaa;
            padding: 8px;
            border-radius: 5px;
        """)


# Зеленый стиль
class GreenStyle(WidgetStyle):

    def apply(self, widget):
        widget.setStyleSheet("""
            background-color: #228b22;
            color: white;
            border: 2px solid #145214;
            padding: 8px;
            border-radius: 5px;
        """)


# Абстрактный класс создателя
class WidgetCreator(ABC):

    def __init__(self, style):
        self.style = style

    @abstractmethod
    def create(self, text):
        pass


# Создание кнопки
class ButtonCreator(WidgetCreator):

    def create(self, text):
        widget = QPushButton(text)
        self.style.apply(widget)
        return widget


# Создание надписи
class LabelCreator(WidgetCreator):

    def create(self, text):
        widget = QLabel(text)
        self.style.apply(widget)
        return widget


# Создание поля ввода
class LineEditCreator(WidgetCreator):

    def create(self, text):
        widget = QLineEdit()
        widget.setPlaceholderText(text)
        self.style.apply(widget)
        return widget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Паттерн Мост - PyQt6")
        self.setMinimumSize(450, 350)

        main_layout = QVBoxLayout()

        # Выбор виджета
        main_layout.addWidget(QLabel("Выберите виджет:"))

        self.widget_combo = QComboBox()
        self.widget_combo.addItems([
            "Кнопка",
            "Надпись",
            "Поле ввода"
        ])
        main_layout.addWidget(self.widget_combo)

        # Выбор стиля
        main_layout.addWidget(QLabel("Выберите стиль:"))

        self.style_combo = QComboBox()
        self.style_combo.addItems([
            "Темный",
            "Светлый",
            "Зеленый"
        ])
        main_layout.addWidget(self.style_combo)

        # Ввод текста
        main_layout.addWidget(QLabel("Введите текст:"))

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Введите текст...")
        main_layout.addWidget(self.text_input)

        # Кнопка создания
        self.create_button = QPushButton("Создать виджет")
        main_layout.addWidget(self.create_button)

        # Область предпросмотра
        self.preview_box = QGroupBox("Предпросмотр")
        self.preview_layout = QVBoxLayout()
        self.preview_box.setLayout(self.preview_layout)

        main_layout.addWidget(self.preview_box)

        self.setLayout(main_layout)

        self.create_button.clicked.connect(self.create_widget)

    def create_widget(self):

        # Получаем выбранный стиль
        styles = {
            "Темный": DarkStyle(),
            "Светлый": LightStyle(),
            "Зеленый": GreenStyle()
        }

        style = styles[self.style_combo.currentText()]

        # Получаем текст
        text = self.text_input.text()

        if not text:
            text = "Пример виджета"

        # Выбираем создателя виджета
        creators = {
            "Кнопка": ButtonCreator,
            "Надпись": LabelCreator,
            "Поле ввода": LineEditCreator
        }

        creator_class = creators[self.widget_combo.currentText()]

        creator = creator_class(style)

        # Создаем виджет
        widget = creator.create(text)

        # Удаляем предыдущий предпросмотр
        while self.preview_layout.count():
            item = self.preview_layout.takeAt(0)
            old_widget = item.widget()

            if old_widget:
                old_widget.deleteLater()

        # Добавляем новый виджет
        self.preview_layout.addWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
