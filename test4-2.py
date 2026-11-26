from abc import ABC, abstractmethod
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class DocumentWidget(ABC):
    @abstractmethod
    def open_file(self, path: str): ...

    @abstractmethod
    def save_file(self, path: str): ...

    @abstractmethod
    def print_document(self): ...

    @abstractmethod
    def send_by_email(self, address: str): ...


class ImageViewer(DocumentWidget):
    def __init__(self):
        self.label = QLabel()

    def open_file(self, path: str):
        self.label.setPixmap(QPixmap(path))

    def save_file(self, path: str):
        pass

    def print_document(self):
        pass

    def send_by_email(self, address: str):
        pass

    # SOLID нарушен тут класс зависит от методов родительского класса которые ему не нужны тоесть Имейдж виевер может только открывать но остальные методы он не может реализовать 