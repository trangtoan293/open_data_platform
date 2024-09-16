import os
import subprocess
from dotenv import load_dotenv
# from src.utils.utils import log_info

##########################################################################################
# log_info('Tải biến môi trường từ file .env')
load_dotenv()

# Đọc thông tin đăng nhập từ biến môi trường
DB_HOST = os.getenv('TRINO_HOST')
DB_PORT = os.getenv('TRINO_PORT')
DB_NAME = os.getenv('TRINO_DB_NAME')
DB_USER = os.getenv('TRINO_USER')

# log_info('Tạo thư mục cho dự án dbt')
import os 
dbt_project_dir = os.path.dirname(os.path.realpath(__file__))

# os.makedirs(dbt_project_dir, exist_ok=True)
# log_info('Di chuyển vào thư mục dự án dbt')
# os.chdir(dbt_project_dir)
subprocess.run(['dbt', 'init', 'open_data_platform'])
# log_info('Đã khởi tạo dự án dbt repo cho open_data_platform')
os.chdir(os.path.join(dbt_project_dir, 'open_data_platform'))
profiles_content = f"""
open_data_platform:
  target: dev
  outputs:
    dev:
      type: trino
      method: none
      host: {DB_HOST}
      port: {DB_PORT}
      user: {DB_USER}
      catalog: {DB_NAME}
      schema: crm
      threads: 2
"""
with open('profiles.yml', 'w') as f:
    f.write(profiles_content)
# ##########################################################################################
# profiles_path = os.path.join(os.path.expanduser('~'), '.dbt', 'profiles.yml')
# profiles_content = f"""
# open_data_platform:
#   target: dev
#   outputs:
#     dev:
#       type: trino
#       method: none
#       host: {DB_HOST}
#       port: {DB_PORT}
#       user: {DB_USER}
#       catalog: {DB_NAME}
#       schema: crm
#       threads: 2
# """
# with open(profiles_path, 'w') as f:
#     f.write(profiles_content)
# # log_info('Đã cập nhật file profiles.yml')

# ##########################################################################################
# dbt_project_path = os.path.join(dbt_project_dir, 'open_data_platform', 'dbt_project.yml')
# with open(dbt_project_path, 'r') as f:
#     dbt_project_content = f.read()
# dbt_project_content = dbt_project_content.replace(
#     "profile: 'open_data_platform'",
#     "profile: 'open_data_platform'\n\n# Specify adapter\nquoting:\n  database: false\n  schema: false\n  identifier: false"
# )
# with open(dbt_project_path, 'w') as f:
#     f.write(dbt_project_content)
# # log_info('Đã cập nhật file dbt_project.yml')
# print("Dự án dbt đã được khởi tạo và cấu hình thành công!")