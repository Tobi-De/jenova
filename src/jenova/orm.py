import inspect
import sqlite3

SQLITE_TYPE_MAP: dict[type, str] = {
    int: "INTEGER",
    float: "REAL",
    str: "TEXT",
    bytes: "BLOB",
    bool: "INTEGER",  # 0 or 1
}


class Table:
    def __init__(self, **kwargs):
        self._data = {
            "id": None
        }

        for key, value in kwargs.items():
            self._data[key] = value

    def __getattribute__(self, key):
        _data = super().__getattribute__("_data")
        if key in _data:
            return _data[key]
        return super().__getattribute__(key)

    @classmethod
    def _get_create_sql(cls):
        CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS {name} ({fields});"
        fields = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
        ]

        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(f"{name} {field.sql_type}")
            elif isinstance(field, ForeignKey):
                fields.append(f"{name}_id INTEGER")

        fields = ", ".join(fields)
        name = cls.__name__.lower()
        return CREATE_TABLE_SQL.format(name=name, fields=fields)


class Database:
    def __init__(self, path: str):
        self.conn = sqlite3.Connection(path)

    @property
    def tables(self):
        SELECT_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type = 'table';"
        return [x[0] for x in self.conn.execute(SELECT_TABLES_SQL).fetchall()]

    def create(self, table: Table):
        self.conn.execute(table._get_create_sql())

    def save(self, instance):
        pass

    def _get_insert_sql(self):
        INSERT_SQL = "INSERT INTO {name} ({fields}) VALUES ({placeholders});"
        cls = self.__class__
        fields = []
        placeholders = []
        values = []

        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
                values.append(getattr(self, name))
                placeholders.append("?")
            elif isinstance(field, ForeignKey):
                fields.append(name + "_id")
                values.append(getattr(self, name).id)
                placeholders.append("?")

        fields = ", ".join(fields)
        placeholders = ", ".join(placeholders)

        sql = INSERT_SQL.format(name=cls.__name__.lower(), fields=fields, placeholders=placeholders)

        return sql, values


class Column:
    def __init__(self, column_type: type):
        self.type = column_type

    @property
    def sql_type(self):
        return SQLITE_TYPE_MAP[self.type]


class ForeignKey:
    def __init__(self, table: Table):
        self.table = table
