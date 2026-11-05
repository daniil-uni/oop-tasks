
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLineEdit, QComboBox, QCheckBox,
    QVBoxLayout
)


# 1. Строитель кнопок
class ButtonBuilder:

    def build(self, text, width, height, color, enabled):
        button = QPushButton(text)
        button.setFixedSize(width, height)
        button.setStyleSheet(f"background-color: {color};")
        button.setEnabled(enabled)

        return button


# 2. Строитель полей ввода
class LineEditBuilder:

    def build(self, text, placeholder, width, read_only):
        field = QLineEdit()
        field.setText(text)
        field.setPlaceholderText(placeholder)
        field.setFixedWidth(width)
        field.setReadOnly(read_only)

        return field


# 3. Строитель выпадающих списков
class ComboBoxBuilder:

    def build(self, items, current_index, width, enabled):
        combo = QComboBox()
        combo.addItems(items)
        combo.setCurrentIndex(current_index)
        combo.setFixedWidth(width)
        combo.setEnabled(enabled)

        return combo


# 4. Строитель флажков
class CheckBoxBuilder:

    def build(self, text, checked, enabled):
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)
        checkbox.setEnabled(enabled)

        return checkbox


# 5. Директор
class WidgetDirector:

    def __init__(self, builder):
        self.builder = builder

    def create_widget(self, **params):
        return self.builder.build(**params)


# Главное окно
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Паттерн Строитель")
        self.resize(400, 450)

        self.layout = QVBoxLayout(self)

        # Кнопки создания виджетов
        button1 = QPushButton("Создать кнопку")
        button2 = QPushButton("Создать поле ввода")
        button3 = QPushButton("Создать список")
        button4 = QPushButton("Создать флажок")

        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)
        self.layout.addWidget(button4)

        # Создаём строителей
        self.button_builder = ButtonBuilder()
        self.line_builder = LineEditBuilder()
        self.combo_builder = ComboBoxBuilder()
        self.checkbox_builder = CheckBoxBuilder()

        # Создаём директора
        self.button_director = WidgetDirector(self.button_builder)
        self.line_director = WidgetDirector(self.line_builder)
        self.combo_director = WidgetDirector(self.combo_builder)
        self.checkbox_director = WidgetDirector(self.checkbox_builder)

        # Подключаем действия
        button1.clicked.connect(self.create_button)
        button2.clicked.connect(self.create_line)
        button3.clicked.connect(self.create_combo)
        button4.clicked.connect(self.create_checkbox)

    # Создание кнопки
    def create_button(self):
        widget = self.button_director.create_widget(
            text="Новая кнопка",
            width=150,
            height=40,
            color="lightgreen",
            enabled=True
        )

        self.layout.addWidget(widget)

    # Создание поля ввода
    def create_line(self):
        widget = self.line_director.create_widget(
            text="",
            placeholder="Введите текст",
            width=200,
            read_only=False
        )

        self.layout.addWidget(widget)

    # Создание выпадающего списка
    def create_combo(self):
        widget = self.combo_director.create_widget(
            items=["Python", "Java", "C++"],
            current_index=0,
            width=200,
            enabled=True
        )

        self.layout.addWidget(widget)

    # Создание флажка
    def create_checkbox(self):
        widget = self.checkbox_director.create_widget(
            text="Согласен с условиями",
            checked=False,
            enabled=True
        )

        self.layout.addWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
