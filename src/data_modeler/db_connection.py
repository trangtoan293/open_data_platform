from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector

class DBConnection:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.metadata = MetaData()
        self.inspector = Inspector.from_engine(self.engine)

    def get_tables(self):
        return self.inspector.get_table_names()

    def get_columns(self, table_name):
        return self.inspector.get_columns(table_name)

    def get_metadata(self):
        metadata = {}
        for table_name in self.get_tables():
            columns = self.get_columns(table_name)
            metadata[table_name] = {
                col['name']: col['type'].__str__() for col in columns
            }
        return metadata