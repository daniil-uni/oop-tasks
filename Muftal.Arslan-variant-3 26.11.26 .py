3 Вариант 

Задание 1
Class Logger:
	instance = None
	_messages_ = []

def __new__(cls):
	if cls._instance is None:
		cls._instance = super().__new__(cls)
	return cls._instance

def log(self, level; str, message: str):
	self._messages.append(f"[{level}] {message}")

def get_messages(self, level: str | None = None):
	if level is None;
		return self._messages
	return [msg for msg in self._messages if msg.startswith(f"[{level}]")]
		
def login(user: str):
	Logger().log('INFO', f'Пользватель{user}')

def pay(user;str, amount: int):
	if amount <=0:
		logger().log('ERROR', f'Неверная сумма у {user}: {amount}
	else:
		logger().log('INFO', f'{user} оплатил {amount} тг')

if__name__=='__main__':
	login('Айбек')	
	login('Айбек', 5000)
	login('Айбек', -10)
	print(Logger() is Logger())
	print(*Logger().get_messages(),sep='\n')	
	print('Ошибок:', len(Logger().get_messages('ERROR')))

Ожидаемый вывод:

True
[INFO] Пользователь Айбек вошел
[INFO] Айбек оплатил 5000 тг
[ERROR] Неверная сумма у Айбек: -10
Ошибок: 1

Задание 2

from abc import ABC abstractmethod
from PyQtWidgets import QWidget, QTextEdit, qPushButton, QVBoxLayout

class Storage(ABC):
	@abstractmethod
	def save(self, text; tr) -> None: ...

class FileStorage(Storage):
	def__Init__(self, path: str):
		self.path = path

	def save(self, text: str) -> None:
		with open(self.path, 'W', encodeng='utf-8') as f:

class NoteWindow(QWidget):
	def__init__(self , storage: Storage):
		super().__init__()
		self.storage = storage
		self.editor = QTextEdit()
		btn = QPushButton('Сохранить')
		btn.clicked.connect(self.on_save)
		layour = QVBoxLayout(self)
		Layout.addWidget(self.editor)
		Layout.addWidget(btn)

	def on_save(self):
		self.storage.save(self.editor.toPlainText())

# Window = NoteWindow(FeleStorage('notes.txt'))

#Ответ:В коде нарушен DIP - принцип инверсии зависимости

#Почему:По условию NoteWindow должен принимать обьект storage: Но в методе on_save прописано создание конкретного класса FeleStorage напрямую завязано на сохранение в текстовый файл и не может нормально работать 

#что бы исправить нужно передать готовый обьект хранилища  при создании вызове (di)  либо сделать так что бы NoteWindow работал с переданным self.storage без хардкора в FileStorage внутри on_save 