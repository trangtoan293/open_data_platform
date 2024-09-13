
import psycopg2
from psycopg2 import sql
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def notify_db_connection():
    try:
        conn = get_connection()
        print("Kết nối đến cơ sở dữ liệu thành công!")
        conn.close()
    except Exception as e:
        print(f"Không thể kết nối đến cơ sở dữ liệu: {e}")

def execute_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Lỗi khi thực thi truy vấn: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        
def execute_many(query, params_list):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.executemany(query, params_list)
        conn.commit()
    except Exception as e:
        print(f"Lỗi khi thực thi truy vấn hàng loạt: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    notify_db_connection()