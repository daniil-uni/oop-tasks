#Вариант 2
#Задание 1
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
		return sql = ';'


class QueryBuilder(ABC):
	@abstractmethod
	def select(self, *columns: str):
		if columns is None:
			columns = "*"
		else:
			self.columns = columns
		return self.columns
		
	@abstractmethod
	def from_table(self, table: str):
		self.table = table
		return self.table

	@abstractmethod
	def where(self, condition: str):
		self.conditions = []
		self.conditions.append(condition)
		return self.conditions

	@abstractmethod
	def order_by(self, column: str):
		self.column = column
		return self.column

	@abstractmethod
	def limit(self, n: int):
		if n < 0:
			raise ValueError("Значение меньше 0")
		else:
			self.n = n
		return n

	@abstractmethod
	def build(self) -> Query:
		if table is None:
			raise ValueError("Укажите таблицу")
		else: 
			return Query

class QueryDirector(QueryBuilder):
	def active_users(self, builder):
		return (builder
			.select('id', 'name')
			.from_table('products')
			.where('active = 1','age >=18')
			.order_by('name')
			.limit(10)
			.build()
		

if __name__ == '__main__':
	b = SqlQueryBuilder()

	print(b.from_table('products').build().to_sql())
	print(QueryDirector().active_users(b).to_sql())

	try:
		b.select('id').build()
	except ValueError as e:
		print('Ошибка:', e)



#Задание 2

from PyQt6.QtGui import QPainter
from PyQt6.QtWidget import QWidget

class Canvas(QWidget):
	def __init__(self, shapes: list[dict]):
	super().__init__()
	self.shapes = shapes

	def paintEvent(self,event)
	painter = QPainter(self)
	
