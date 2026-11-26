from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Query:
    table: str
    columns: list = field(default_factory=lambda: ["*"])
    conditions: list = field(default_factory=list)
    order: str = ""
    limit: int = None

    def to_sql(self):
        sql = f"SELECT {', '.join(self.columns)} FROM {self.table}"

        if self.conditions:
            sql += " WHERE " + " AND ".join(self.conditions)

        if self.order:
            sql += f" ORDER BY {self.order}"

        if self.limit is not None:
            sql += f" LIMIT {self.limit}"

        return sql + ";"


class QueryBuilder(ABC):

    @abstractmethod
    def select(self, *columns): pass

    @abstractmethod
    def from_table(self, table): pass

    @abstractmethod
    def where(self, condition): pass

    @abstractmethod
    def order_by(self, column): pass

    @abstractmethod
    def limit(self, n): pass

    @abstractmethod
    def build(self): pass


class SQLQueryBuilder(QueryBuilder):

    def __init__(self):
        self.table = ""
        self.columns = ["*"]
        self.conditions = []
        self.order = ""
        self.max_limit = None

    def select(self, *columns):
        self.columns = list(columns) if columns else ["*"]
        return self

    def from_table(self, table):
        self.table = table
        return self

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def order_by(self, column):
        self.order = column
        return self

    def limit(self, n):
        self.max_limit = n
        return self

    def build(self):
        if not self.table:
            raise ValueError("Не указана таблица")

        return Query(
            self.table,
            self.columns,
            self.conditions,
            self.order,
            self.max_limit
        )


if __name__ == "__main__":
    b = SQLQueryBuilder()

    query = (b.select("id", "name")
             .from_table("users")
             .where("active = 1")
             .where("age >= 18")
             .order_by("name")
             .limit(10)
             .build())

    print(query.to_sql())

    try:
        b = SQLQueryBuilder()
        b.select("id").build()
    except ValueError as e:
        print("Ошибка:", e)