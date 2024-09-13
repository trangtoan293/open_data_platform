import os
from dotenv import load_dotenv

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