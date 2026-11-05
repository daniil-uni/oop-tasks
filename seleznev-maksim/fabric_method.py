
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QPushButton, QVBoxLayout, QHBoxLayout
)


class ButtonFactory:

    @staticmethod
    def create_button(text, color, width, height, parent=None):
        button = QPushButton(text, parent)
        button.setStyleSheet(f"background-color: {color};")
        button.setFixedSize(width, height)

        return button


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фабрика кнопок")
        self.resize(600, 350)

        central = QWidget()
        self.layout = QVBoxLayout(central)

        # Горизонтальное расположение новых кнопок
        self.buttons_layout = QHBoxLayout()

        self.layout.addLayout(self.buttons_layout)

        self.setCentralWidget(central)

        # Основные кнопки
        button1 = QPushButton("Создать зелёную кнопку")
        button2 = QPushButton("Создать красную кнопку")
        button3 = QPushButton("Создать синюю кнопку")

        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)

        # Действия кнопок
        button1.clicked.connect(self.create_green)
        button2.clicked.connect(self.create_red)
        button3.clicked.connect(self.create_blue)

    def create_green(self):
        button = ButtonFactory.create_button(
            "Зелёная кнопка", "green", 150, 40
        )
        button.clicked.connect(
            lambda: button.setText("Нажата!")
        )
        self.buttons_layout.addWidget(button)

    def create_red(self):
        button = ButtonFactory.create_button(
            "Красная кнопка", "red", 150, 40
        )
        button.clicked.connect(
            lambda: button.setText("Нажата!")
        )
        self.buttons_layout.addWidget(button)

    def create_blue(self):
        button = ButtonFactory.create_button(
            "Синяя кнопка", "blue", 150, 40
        )
        button.clicked.connect(
            lambda: button.setText("Нажата!")
        )
        self.buttons_layout.addWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
