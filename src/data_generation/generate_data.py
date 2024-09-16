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

ticket_ids = []
campaign_ids = []

def generate_campaign_data(num_records):
    global campaign_ids
    data = []
    for _ in range(num_records):
        campaign_id = random.randint(1, 10000)
        campaign_ids.append(campaign_id)
        data.append((
            campaign_id,
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
        INSERT INTO crm.campaign (campaign_id, name, description, time_limit, status, type, 
        is_call_type, is_sms_type, is_email_type, start_date, end_date, 
        dialer_type, predictive_dialer_id, survey_id, created_by, created_date, 
        import_status, sms_scheduler_id, sms_run_status, email_scheduler_id, 
        email_run_status, ticket_type_id, notice_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s)
    """, data)
    return campaign_ids

def generate_ticket_data(num_records, campaign_ids):
    global ticket_ids
    data = []
    for _ in range(num_records):
        ticket_id = random.randint(1, 1000000)
        campaign_id = random.choice(campaign_ids)
        ticket_ids.append(ticket_id)
        data.append((
            ticket_id,
            fake.name(),
            fake.name(),
            random.choice(['Individual', 'Corporate']),
            fake.phone_number(),
            fake.phone_number(),
            fake.phone_number(),
            fake.phone_number(),
            fake.street_address(),
            fake.street_address(),
            fake.street_address(),
            fake.street_name(),
            random.choice(cities),
            random.choice(cities),
            random.choice(cities),
            random.choice(cities),
            random.choice(provinces),
            random.choice(provinces),
            random.choice(provinces),
            fake.email(),
            fake.bothify(text='CONTRACT-#####'),
            fake.date_time_between(start_date='-2y', end_date='now'),
            fake.bothify(text='ID########'),
            random.randint(10000000, 1000000000),
            random.randint(6, 60),
            random.randint(1000000, 100000000),
            random.randint(1000000, 100000000),
            random.randint(1, 60),
            random.randint(100000, 10000000),
            random.randint(100000, 10000000),
            random.randint(0, 1000000),
            fake.date_time_between(start_date='now', end_date='+1y'),
            random.randint(0, 90),
            random.randint(1000000, 100000000),
            fake.bothify(text='PROD###'),
            float(random.randint(1, 1000)),
            campaign_id,
            fake.bothify(text='PRED###'),
            fake.bothify(text='SURV###'),
            fake.sentence(),
            fake.sentence(),
            random.randint(1, 10),
            fake.text(),
            fake.date_time_this_year(),
            fake.bothify(text='ROOM###'),
            float(random.randint(1, 1000)),
            fake.date_time_this_month(),
            random.choice(['Pending', 'In Progress', 'Resolved']),
            fake.text(),
            fake.name(),
            fake.date_time_this_year(),
            random.randint(1, 1000),
            fake.date_time_this_year(),
            float(random.randint(1, 1000)),
            fake.date_time_this_year(),
            random.choice(['Open', 'Closed', 'Pending']),
            float(random.randint(1, 10)),
            random.randint(1, 1000),
            random.choice(['Yes', 'No']),
            random.randint(1, 1000),
            random.choice(['Yes', 'No']),
            random.choice(['Support', 'Complaint', 'Inquiry']),
            fake.date_time_this_year(),
            random.choice(['Yes', 'No']),
            random.randint(1, 60),
            random.randint(1000000, 100000000),
            random.randint(1000000, 100000000),
            fake.date_time_this_year(),
            random.randint(0, 100000000),
            fake.date_time_this_month(),
            float(random.randint(1000000, 10000000))
        ))
    
    num_columns = len(data[0])
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
    return ticket_ids

def generate_cdr_data(num_records, ticket_ids, campaign_ids):
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
            str(random.choice(campaign_ids)),
            str(random.choice(ticket_ids)),
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

def generate_paired_data(num_records, ticket_ids):
    data = []
    for _ in range(num_records):
        data.append((
            random.choice(ticket_ids),
            random.randint(100000, 1000000),
            fake.date_between(start_date='-1y', end_date='today'),
            random.randint(1, 100)
        ))
    execute_many("""
        INSERT INTO crm.paired (ticket_id, amt_paired, date_paired, employee_id)
        VALUES (%s, %s, %s, %s)
    """, data)


def truncate_all_tables():
    tables = ['campaign', 'ticket', 'cdr', 'paired']
    for table in tables:
        execute_query(f"TRUNCATE TABLE crm.{table} RESTART IDENTITY CASCADE;")
    print("Đã xóa toàn bộ dữ liệu từ các bảng.")

if __name__ == "__main__":
    truncate_all_tables() # Xóa toàn bộ dữ liệu từ các bảng
    campaign_ids = generate_campaign_data(100)  # Tạo 100 bản ghi cho bảng campaign
    ticket_ids = generate_ticket_data(1000, campaign_ids)  # Tạo 1000 bản ghi cho bảng ticket
    generate_cdr_data(1000, ticket_ids, campaign_ids)  # Tạo 1000 bản ghi cho bảng cdr
    generate_paired_data(1000, ticket_ids)  # Tạo 1000 bản ghi cho bảng paired
    print("Đã tạo và chèn dữ liệu giả thành công!")