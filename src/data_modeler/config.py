import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
# Tải các biến môi trường từ file .env
load_dotenv()

# Đọc thông tin đăng nhập cơ sở dữ liệu từ biến môi trường
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

new_password = quote_plus(DB_CONFIG['password'])
# Tạo chuỗi kết nối cơ sở dữ liệu
connection_string = f"postgresql://{DB_CONFIG['user']}:{new_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
print(connection_string)

