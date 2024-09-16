import sys
from db_connection import DBConnection
from workspace_ui import WorkspaceUI
from data_mapping import DataMapping
from data_storage import DataStorage
from config import connection_string

def main():
    # Kết nối đến cơ sở dữ liệu nguồn
    source_db = DBConnection(connection_string)
    source_metadata = source_db.get_metadata()

    # Khởi tạo và chạy giao diện người dùng Taipy
    ui = WorkspaceUI(source_metadata)
    ui.run()

    # Sau khi người dùng hoàn thành mô hình:
    mappings = ui.get_mappings()

    # Lưu trữ kết quả
    storage = DataStorage(connection_string)
    storage.save_to_db(mappings)
    storage.save_to_yaml(mappings, 'data_model.yaml')

if __name__ == '__main__':
    main()