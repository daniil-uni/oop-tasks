# 3 вариант

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'messages'):
            self.messages = []

    def log(self, level, message):
        self.messages.append(f'[{level}] {message}')

    def get_messages(self, level=None):
        if level is None:
            return self.messages
        return [m for m in self.messages if m.startswith(f'[{level}]')]

def login(user: str):
    Logger().log('INFO', f'Пользователь {user} вошел')

def pay(user: str, amount: int):
    if amount <= 0:
        Logger().log('ERROR', f'Неверная сумма у {user}: {amount}')
    else:
        Logger().log('INFO', f'{user} оплатил {amount} тг')


if __name__ == '__main__':
    login('Айбек')
    pay('Айбек', 5000)
    pay('Айбек', -10)
    print(Logger() is Logger())
    print(*Logger().get_messages(), sep='\n')
    print('Ошибок:', len(Logger().get_messages('ERROR')))