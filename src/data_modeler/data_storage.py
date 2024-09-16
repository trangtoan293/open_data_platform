import yaml
from sqlalchemy import Table, Column, MetaData, create_engine
from sqlalchemy.types import String, Integer, Float

class DataStorage:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.metadata = MetaData()

    def save_to_db(self, mappings):
        for source_table, target_tables in mappings.items():
            for target_table, column_mappings in target_tables.items():
                columns = [Column(col_name, self._get_column_type(col_type)) 
                           for col_name, col_type in column_mappings.items()]
                Table(target_table, self.metadata, *columns)
        
        self.metadata.create_all(self.engine)

    def save_to_yaml(self, mappings, file_path):
        with open(file_path, 'w') as file:
            yaml.dump(mappings, file)

    def _get_column_type(self, type_str):
        type_map = {
            'INTEGER': Integer,
            'VARCHAR': String,
            'FLOAT': Float,
            # Thêm các kiểu dữ liệu khác nếu cần
        }
        return type_map.get(type_str.upper(), String)