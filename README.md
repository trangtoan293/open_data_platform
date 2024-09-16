# Open Data Platform

Đây là một dự án nền tảng dữ liệu mở sử dụng dbt (data build tool) để chuyển đổi và mô hình hóa dữ liệu.

## Cấu trúc dự án

Dự án được tổ chức như sau:

- `src/`: Thư mục chứa mã nguồn chính
  - `data_generation/`: Mã để tạo dữ liệu mẫu
  - `data_transformation/`: Mã để chuyển đổi dữ liệu sử dụng dbt
  - `utils/`: Các tiện ích và hàm hỗ trợ

## Cài đặt

1. Cài đặt các phụ thuộc:
   ```
   pip install -r requirements.txt
   ```

2. Cấu hình kết nối cơ sở dữ liệu trong tệp `.env`

3. Khởi tạo dự án dbt:
   ```
   dbt init open_data_platform
   ```

## Sử dụng

### Tạo dữ liệu mẫu

Chạy script `generate_data.py` để tạo dữ liệu mẫu:

```
python src/data_generation/generate_data.py
```

### Chuyển đổi dữ liệu với dbt

1. Di chuyển vào thư mục dự án dbt:
   ```
   cd src/data_transformation/open_data_platform
   ```

2. Chạy các mô hình dbt:
   ```
   dbt run
   ```

3. Kiểm tra các mô hình:
   ```
   dbt test
   ```

## Mô hình dữ liệu

Dự án bao gồm các mô hình staging sau:

- `stg_ticket`: Dữ liệu vé hỗ trợ
- `stg_campaign`: Dữ liệu chiến dịch
- `stg_paired`: Dữ liệu ghép cặp
- `stg_call`: Dữ liệu cuộc gọi

## Đóng góp

Nếu bạn muốn đóng góp vào dự án, vui lòng tạo một pull request hoặc mở một issue để thảo luận về các thay đổi đề xuất.

## Giấy phép

[Thêm thông tin về giấy phép của dự án ở đây]
