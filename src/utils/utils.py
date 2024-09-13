import logging
import os
from datetime import datetime

def setup_logger(name, log_file, level=logging.INFO):
    """Hàm thiết lập logger"""
    # Tạo thư mục logs nếu chưa tồn tại
    log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Tạo đường dẫn đầy đủ cho file log
    log_path = os.path.join(log_dir, log_file)
    
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    
    handler = logging.FileHandler(log_path, encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Tạo logger chung cho toàn bộ ứng dụng
app_logger = setup_logger('app_logger', f'app_{datetime.now().strftime("%Y%m%d")}.log')

def log_info(message):
    """Ghi log thông tin"""
    app_logger.info(message)

def log_error(message):
    """Ghi log lỗi"""
    app_logger.error(message)

def log_debug(message):
    """Ghi log gỡ lỗi"""
    app_logger.debug(message)