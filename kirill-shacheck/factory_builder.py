import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class ButtonFactory:
    """Фабрика для создания стилизованных кнопок."""

    @staticmethod
    def create_button(
        text: str = "Кнопка",
        color: str = "#333333",
        width: int = 120,
        height: int = 40,
        parent: QWidget | None = None,
    ) -> QPushButton:
        button = QPushButton(text, parent)
        button.setFixedSize(width, height)

        # Подбираем цвет текста в зависимости от фона (для белой/светлой кнопки -  тёмный текст)
        text_color = "#333333" if color in ("white", "#ffffff", "#f5f5f5") else "#ffffff"
        border_color = "#cccccc" if color in ("white", "#ffffff", "#f5f5f5") else "transparent"

        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: {text_color};
                font-size: 15px;
                font-weight: bold;
                border: 2px solid {border_color};
                border-radius: 14px;
            }}
            QPushButton:hover {{
                opacity: 0.9;
                border-color: #999999;
            }}
            QPushButton:pressed {{
                background-color: #555555;
            }}
        """)
        return button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Factoru_Builder")
        self.resize(550, 350)

        # Основной центральный виджет
        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)

        # Информационная надпись
        self.status_label = QLabel("Нажмите кнопку на панели управления для создания новой кнопки.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 13px; color: #555; margin: 10px;")
        self.main_layout.addWidget(self.status_label)

        # Панель управления (кнопки добавления)
        controls_layout = QHBoxLayout()
        add_delete_btn = QPushButton("+ Добавить Delete")
        add_cancel_btn = QPushButton("+ Добавить Cancel")
        add_save_btn = QPushButton("+ Добавить Save")

        controls_layout.addWidget(add_delete_btn)
        controls_layout.addWidget(add_cancel_btn)
        controls_layout.addWidget(add_save_btn)
        self.main_layout.addLayout(controls_layout)

        # Контейнер для отображения динамически созданных кнопок
        self.buttons_container_layout = QHBoxLayout()
        self.buttons_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.buttons_container_layout)
        self.main_layout.addStretch()

        self.setCentralWidget(central_widget)

        # Подключение сигналов панели управления
        add_delete_btn.clicked.connect(self.create_delete_button)
        add_cancel_btn.clicked.connect(self.create_cancel_button)
        add_save_btn.clicked.connect(self.create_save_button)

    def create_delete_button(self):
        btn = ButtonFactory.create_button(
            text="Delete",
            color="#c0392b",  # Красный
            width=110,
            height=42,
            parent=self,
        )
        btn.clicked.connect(lambda: self.on_button_action("Удаление: объект успешно удалён!"))
        self.buttons_container_layout.addWidget(btn)

    def create_cancel_button(self):
        btn = ButtonFactory.create_button(
            text="Cancel",
            color="#ffffff",  # Белый
            width=110,
            height=42,
            parent=self,
        )
        btn.clicked.connect(lambda: self.on_button_action("Отмена: операция сброшена."))
        self.buttons_container_layout.addWidget(btn)

    def create_save_button(self):
        btn = ButtonFactory.create_button(
            text="Save",
            color="#2d3436",  # Тёмно-серый / Чёрный
            width=110,
            height=42,
            parent=self,
        )
        btn.clicked.connect(lambda: self.on_button_action("Сохранение: данные сохранены!"))
        self.buttons_container_layout.addWidget(btn)

    def on_button_action(self, message: str):
        self.status_label.setText(f"Событие: {message}")
        QMessageBox.information(self, "Действие", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())