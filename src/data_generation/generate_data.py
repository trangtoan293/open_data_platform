from faker import Faker
import random
from datetime import datetime, timedelta
from database import execute_query, execute_many

fake = Faker('vi_VN')
provinces = [
    'Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng', 'Hải Phòng', 'Cần Thơ',
    'An Giang', 'Bà Rịa - Vũng Tàu', 'Bắc Giang', 'Bắc Kạn', 'Bạc Liêu',
    'Bắc Ninh', 'Bến Tre', 'Bình Định', 'Bình Dương', 'Bình Phước',
    'Bình Thuận', 'Cà Mau', 'Cao Bằng', 'Đắk Lắk', 'Đắk Nông',
    'Điện Biên', 'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Giang',
    'Hà Nam', 'Hà Tĩnh', 'Hải Dương', 'Hậu Giang', 'Hòa Bình',
    'Hưng Yên', 'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu',
    'Lâm Đồng', 'Lạng Sơn', 'Lào Cai', 'Long An', 'Nam Định',
    'Nghệ An', 'Ninh Bình', 'Ninh Thuận', 'Phú Thọ', 'Quảng Bình',
    'Quảng Nam', 'Quảng Ngãi', 'Quảng Ninh', 'Quảng Trị', 'Sóc Trăng',
    'Sơn La', 'Tây Ninh', 'Thái Bình', 'Thái Nguyên', 'Thanh Hóa',
    'Thừa Thiên Huế', 'Tiền Giang', 'Trà Vinh', 'Tuyên Quang', 'Vĩnh Long',
    'Vĩnh Phúc', 'Yên Bái', 'Phú Yên'
]

cities = [
    'Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng', 'Hải Phòng', 'Cần Thơ',
    'Biên Hòa', 'Nha Trang', 'Huế', 'Đà Lạt', 'Vũng Tàu',
    'Qui Nhơn', 'Buôn Ma Thuột', 'Vinh', 'Thái Nguyên', 'Nam Định',
    'Việt Trì', 'Hạ Long', 'Thanh Hóa', 'Phan Thiết', 'Cà Mau'
]
# Danh sách để lưu trữ các ID đã tạo
ticket_ids = []
campaign_ids = []

# Hàm tạo dữ liệu giả cho bảng campaign
def generate_campaign_data(num_records):
    data = []
    for _ in range(num_records):
        data.append((
            random.randint(1, 1000),
            fake.name(),
            fake.text(),
            fake.time(),
            random.choice(['active', 'inactive']),
            random.choice(['call', 'sms', 'email']),
            str(random.choice([True, False])),
            str(random.choice([True, False])),
            str(random.choice([True, False])),
            fake.date_between(start_date='-1y', end_date='today'),
            fake.date_between(start_date='today', end_date='+1y'),
            random.choice(['predictive', 'progressive']),
            str(random.randint(1, 1000)),
            str(random.randint(1, 1000)),
            random.randint(1, 100),
            fake.date_time_this_year(),
            random.choice(['pending', 'completed']),
            str(random.randint(1, 1000)),
            random.choice(['pending', 'running', 'completed']),
            str(random.randint(1, 1000)),
            random.choice(['pending', 'running', 'completed']),
            random.randint(1, 100),
            str(random.randint(1, 1000))
        ))
    execute_many("""
        INSERT INTO crm.campaign (campaign_id,name, description, time_limit, status, type, 
        is_call_type, is_sms_type, is_email_type, start_date, end_date, 
        dialer_type, predictive_dialer_id, survey_id, created_by, created_date, 
        import_status, sms_scheduler_id, sms_run_status, email_scheduler_id, 
        email_run_status, ticket_type_id, notice_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s)
    """, data)

# Hàm tạo dữ liệu giả cho bảng cdr
def generate_cdr_data(num_records):
    data = []
    for _ in range(num_records):
        data.append((
            fake.date_time_this_year(),
            fake.phone_number(),
            fake.phone_number(),
            fake.phone_number(),
            fake.word(),
            fake.word(),
            fake.word(),
            fake.word(),
            fake.word(),
            random.randint(1, 3600),
            random.randint(1, 3600),
            random.choice(['ANSWERED', 'NO ANSWER', 'BUSY']),
            random.randint(1, 10),
            fake.word(),
            fake.uuid4(),
            fake.word(),
            fake.phone_number(),
            fake.file_name(),
            fake.phone_number(),
            fake.name(),
            fake.phone_number(),
            fake.name(),
            fake.name(),
            fake.word(),
            fake.word(),
            str(random.randint(1, 1000)),
            str(random.randint(1, 1000)),
            fake.name(),
            fake.uuid4(),
            fake.word(),
            fake.word(),
            fake.word()
        ))
    execute_many("""
        INSERT INTO crm.cdr (calldate, clid, src, dst, dcontext, channel, 
        dstchannel, lastapp, lastdata, duration, billsec, disposition, amaflags, 
        accountcode, uniqueid, userfield, did, recordingfile, cnum, cnam, 
        outbound_cnum, outbound_cnam, dst_cnam, project_code, inbound_queue, 
        campaign_id, ticket_id, inbound_agent, inbound_uid, call_route, trunk_name, 
        contract_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, data)

# Hàm tạo dữ liệu giả cho bảng paired
def generate_paired_data(num_records):
    data = []
    for _ in range(num_records):
        data.append((
            random.randint(1000, 9999),  # contract_id
            random.randint(100000, 1000000),  # amt_paired
            fake.date_between(start_date='-1y', end_date='today'),  # date_paired
            random.randint(1, 100)  # employee_id
        ))
    execute_many("""
        INSERT INTO crm.paired (ticket_id, amt_paired, date_paired, employee_id)
        VALUES (%s, %s, %s, %s)
    """, data)

# Hàm tạo dữ liệu giả cho bảng ticket
from datetime import datetime, timedelta

def generate_ticket_data(num_records):
    global ticket_ids, campaign_ids
    data = []
    for _ in range(num_records):
        ticket_id = random.randint(1, 1000000)
        campaign_id = random.randint(1, 10000)
        ticket_ids.append(ticket_id)
        campaign_ids.append(campaign_id)
        data.append((
            ticket_id,  # BIGINT
            fake.name(),  # TEXT
            fake.name(),  # TEXT
            random.choice(['Individual', 'Corporate']),  # TEXT
            fake.phone_number(),  # TEXT
            fake.phone_number(),  # TEXT
            fake.phone_number(),  # TEXT
            fake.phone_number(),  # TEXT
            fake.street_address(),  # TEXT
            fake.street_address(),  # TEXT
            fake.street_address(),  # TEXT
            fake.street_name(),  # TEXT
            random.choice(cities),
            random.choice(cities),
            random.choice(cities),
            random.choice(cities),
            random.choice(provinces),
            random.choice(provinces),
            random.choice(provinces),
            fake.email(),  # TEXT
            fake.bothify(text='CONTRACT-#####'),  # TEXT
            fake.date_time_between(start_date='-2y', end_date='now'),  # TIMESTAMP
            fake.bothify(text='ID########'),  # TEXT
            random.randint(10000000, 1000000000),  # BIGINT
            random.randint(6, 60),  # BIGINT
            random.randint(1000000, 100000000),  # BIGINT
            random.randint(1000000, 100000000),  # BIGINT
            random.randint(1, 60),  # BIGINT
            random.randint(100000, 10000000),  # BIGINT
            random.randint(100000, 10000000),  # BIGINT
            random.randint(0, 1000000),  # BIGINT
            fake.date_time_between(start_date='now', end_date='+1y'),  # TIMESTAMP
            random.randint(0, 90),  # BIGINT
            random.randint(1000000, 100000000),  # BIGINT
            fake.bothify(text='PROD###'),  # TEXT
            float(random.randint(1, 1000)),  # DOUBLE PRECISION
            campaign_id,  # BIGINT
            fake.bothify(text='PRED###'),  # TEXT
            fake.bothify(text='SURV###'),  # TEXT
            fake.sentence(),  # TEXT
            fake.sentence(),  # TEXT
            random.randint(1, 10),  # BIGINT
            fake.text(),  # TEXT
            fake.date_time_this_year(),  # TIMESTAMP
            fake.bothify(text='ROOM###'),  # TEXT
            float(random.randint(1, 1000)),  # DOUBLE PRECISION
            fake.date_time_this_month(),  # TIMESTAMP
            random.choice(['Pending', 'In Progress', 'Resolved']),  # TEXT
            fake.text(),  # TEXT
            fake.name(),  # TEXT
            fake.date_time_this_year(),  # TIMESTAMP
            random.randint(1, 1000),  # BIGINT
            fake.date_time_this_year(),  # TIMESTAMP
            float(random.randint(1, 1000)),  # DOUBLE PRECISION
            fake.date_time_this_year(),  # TIMESTAMP
            random.choice(['Open', 'Closed', 'Pending']),  # TEXT
            float(random.randint(1, 10)),  # DOUBLE PRECISION
            random.randint(1, 1000),  # BIGINT
            random.choice(['Yes', 'No']),  # TEXT
            random.randint(1, 1000),  # BIGINT
            random.choice(['Yes', 'No']),  # TEXT
            random.choice(['Support', 'Complaint', 'Inquiry']),  # TEXT
            fake.date_time_this_year(),  # TIMESTAMP
            random.choice(['Yes', 'No']),  # TEXT
            random.randint(1, 60),  # BIGINT
            random.randint(1000000, 100000000),  # BIGINT
            random.randint(1000000, 100000000),  # BIGINT
            fake.date_time_this_year(),  # TIMESTAMP
            random.randint(0, 100000000),  # BIGINT
            fake.date_time_this_month(),  # TIMESTAMP
            float(random.randint(1000000, 10000000))  # DOUBLE PRECISION
        ))
    
    # Đếm số lượng cột trong dữ liệu
    num_columns = len(data[0])
    
    # Tạo câu lệnh SQL với số lượng placeholders chính xác
    placeholders = ', '.join(['%s'] * num_columns)
    
    sql = f"""
        INSERT INTO crm.ticket (id, name, name_ascii, customer_type, mobile_phone, home_phone,
        office_phone, other_phone, address_interdist, address_interdist1, address_interdist2,
        address_street, address_ward, address_district, address_district1, address_district2,
        province_name, province_name1, province_name2, email, contract_number, date_of_sign,
        id_card_no, principal, tenor, dept, sum_of_payment, count_of_payment, sum_of_panelty,
        sum_of_panelty_paid, the_rest_of_penalty, last_installment, dpd, total_paid, productcode,
        agent_id, campaign_id, predictive_id, survey_id, title, title_ascii, ticket_type_id,
        case_note, follow_up_date, escalate_room_id, escalate_agent_id, escalate_follow_up_date,
        escalate_status, escalate_note, escalate_by, escalate_date, created_by, created_date,
        updated_by, updated_date, status, reason, sms_scheduler_id, is_sms_sent, email_scheduler_id,
        is_email_sent, ticket_category, last_call_datetime, close_ticket, installment, total_payment,
        previous_payment, previous_payment_date, remaining_dept, promise_date, promise_target)
        VALUES ({placeholders})
    """
    
    execute_many(sql, data)

if __name__ == "__main__":
    generate_ticket_data(1000)  # Tạo 1000 bản ghi cho bảng ticket
    generate_paired_data(1000)  # Tạo 1000 bản ghi cho bảng paired
    generate_campaign_data(100)  # Tạo 100 bản ghi cho bảng campaign
    generate_cdr_data(1000)  # Tạo 1000 bản ghi cho bảng cdr
    print("Đã tạo và chèn dữ liệu giả thành công!")