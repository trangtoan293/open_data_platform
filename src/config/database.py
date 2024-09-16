import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }

def get_connection_string():
    config = get_db_config()
    password = quote_plus(config['password'])
    return f"postgresql://{config['user']}:{password}@{config['host']}:{config['port']}/{config['database']}"

print(get_connection_string())