from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Query:
    table: str
    columns: list[str] = field(default_factory=lambda: ['*'])
    conditions: list[str] = field(default_factory=list)
    order: str | None = None
    limit: int | None = None

    def to_sql(self) -> str:
        sql = f"SELECT {', '.join(self.columns)} FROM {self.table}"
        if self.conditions:
            sql += ' WHERE ' + ' AND '.join(self.conditions)
        if self.order:
            sql += f' ORDER BY {self.order}'
        if self.limit is not None:
            sql += f' LIMIT {self.limit}'
        return sql + ';'


class QueryBuilder(ABC):
    @abstractmethod
    def select(self, *columns: str): ...
    @abstractmethod
    def from_table(self, table: str): ...
    @abstractmethod
    def where(self, condition: str): ...
    @abstractmethod
    def order_by(self, column: str): ...
    @abstractmethod
    def limit(self, n: int): ...
    @abstractmethod
    def build(self) -> Query: ...

#--здесь мой код

class SqlQueryBuilder(QueryBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.table = None
        self.columns = ['*']
        self.conditions = []
        self.order = None
        self.limit_val = None

    def select(self, *columns: str):
        self.columns = list(columns)
        return self

    def from_table(self, table: str):
        self.table = table
        return self

    def where(self, condition: str):
        self.conditions.append(condition)
        return self

    def order_by(self, column: str):
        self.order = column
        return self

    def limit(self, n: int):
        self.limit_val = n
        return self

    def build(self) -> Query:
        if not self.table:
            self.reset()
            raise ValueError('не указана таблица')
        q = Query(self.table, self.columns, self.conditions, self.order, self.limit_val)
        self.reset()
        return q


class QueryDirector:
    def active_users(self, builder):
        return (
            builder
            .select('id', 'name')
            .from_table('users')
            .where('active = 1')
            .where('age >= 18')
            .order_by('name')
            .limit(10)
            .build()
        )


if __name__ == '__main__':
    b = SqlQueryBuilder()
    print(b.from_table('products').build().to_sql())
    print(QueryDirector().active_users(b).to_sql())
    try:
        b.select('id').build()
    except ValueError as e:
        print('Ошибка:', e)


from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget

class Canvas(QWidget):
    def __init__(self, shapes: list[dict]):
        super().__init__()
        self.shapes = shapes

    def paintEvent(self, event):
        painter = QPainter(self)
        for s in self.shapes:
            if s['type'] == 'circle':
                painter.drawEllipse(s['x'], s['y'], s['r'] * 2, s['r'] * 2)
            elif s['type'] == 'rect':
                painter.drawRect(s['x'], s['y'], s['w'], s['h'])
            elif s['type'] == 'line':
                painter.drawLine(s['x1'], s['y1'], s['x2'], s['y2'])
            elif s['type'] == 'triangle':
                painter.drawLine(s['x1'], s['y1'], s['x2'], s['y2'])
                painter.drawLine(s['x2'], s['y2'], s['x3'], s['y3'])
                painter.drawLine(s['x3'], s['y3'], s['x1'], s['y1'])
