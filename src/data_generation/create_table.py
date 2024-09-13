from database import execute_query

def create_tables():
    # Tạo schema nếu chưa tồn tại
    execute_query("CREATE SCHEMA IF NOT EXISTS crm;")

    # Tạo bảng campaign
    execute_query("""
    CREATE TABLE IF NOT EXISTS crm.campaign (
        campaign_id BIGINT PRIMARY KEY,
        name TEXT,
        description TEXT,
        time_limit TEXT,
        status TEXT,
        type TEXT,
        is_call_type TEXT,
        is_sms_type TEXT,
        is_email_type TEXT,
        start_date DATE,
        end_date DATE,
        dialer_type TEXT,
        predictive_dialer_id TEXT,
        survey_id TEXT,
        created_by BIGINT,
        created_date TIMESTAMP,
        import_status TEXT,
        sms_scheduler_id TEXT,
        sms_run_status TEXT,
        email_scheduler_id TEXT,
        email_run_status TEXT,
        ticket_type_id BIGINT,
        notice_id TEXT
    );
    """)

    # Tạo bảng cdr
    execute_query("""
    CREATE TABLE IF NOT EXISTS crm.cdr (
        id BIGSERIAL PRIMARY KEY,
        calldate TIMESTAMP,
        clid TEXT,
        src TEXT,
        dst TEXT,
        dcontext TEXT,
        channel TEXT,
        dstchannel TEXT,
        lastapp TEXT,
        lastdata TEXT,
        duration BIGINT,
        billsec BIGINT,
        disposition TEXT,
        amaflags BIGINT,
        accountcode TEXT,
        uniqueid TEXT,
        userfield TEXT,
        did TEXT,
        recordingfile TEXT,
        cnum TEXT,
        cnam TEXT,
        outbound_cnum TEXT,
        outbound_cnam TEXT,
        dst_cnam TEXT,
        project_code TEXT,
        inbound_queue TEXT,
        campaign_id TEXT,
        ticket_id TEXT,
        inbound_agent TEXT,
        inbound_uid TEXT,
        call_route TEXT,
        trunk_name TEXT,
        contract_number TEXT
    );
    """)

    # Tạo bảng paired
    execute_query("""
    CREATE TABLE IF NOT EXISTS crm.paired (
        ticket_id BIGINT,
        amt_paired BIGINT,
        date_paired DATE,
        employee_id BIGINT
    );
    """)

    # Tạo bảng ticket
    execute_query("""
    CREATE TABLE IF NOT EXISTS crm.ticket (
        id BIGINT PRIMARY KEY,
        name TEXT,
        name_ascii TEXT,
        customer_type TEXT,
        mobile_phone TEXT,
        home_phone TEXT,
        office_phone TEXT,
        other_phone TEXT,
        address_interdist TEXT,
        address_interdist1 TEXT,
        address_interdist2 TEXT,
        address_street TEXT,
        address_ward TEXT,
        address_district TEXT,
        address_district1 TEXT,
        address_district2 TEXT,
        province_name TEXT,
        province_name1 TEXT,
        province_name2 TEXT,
        email TEXT,
        contract_number TEXT,
        date_of_sign TIMESTAMP,
        id_card_no TEXT,
        principal BIGINT,
        tenor BIGINT,
        dept BIGINT,
        sum_of_payment BIGINT,
        count_of_payment BIGINT,
        sum_of_panelty BIGINT,
        sum_of_panelty_paid BIGINT,
        the_rest_of_penalty BIGINT,
        last_installment TIMESTAMP,
        dpd BIGINT,
        total_paid BIGINT,
        productcode TEXT,
        agent_id DOUBLE PRECISION,
        campaign_id BIGINT,
        predictive_id TEXT,
        survey_id TEXT,
        title TEXT,
        title_ascii TEXT,
        ticket_type_id BIGINT,
        case_note TEXT,
        follow_up_date TIMESTAMP,
        escalate_room_id TEXT,
        escalate_agent_id DOUBLE PRECISION,
        escalate_follow_up_date TIMESTAMP,
        escalate_status TEXT,
        escalate_note TEXT,
        escalate_by TEXT,
        escalate_date TIMESTAMP,
        created_by BIGINT,
        created_date TIMESTAMP,
        updated_by DOUBLE PRECISION,
        updated_date TIMESTAMP,
        status TEXT,
        reason DOUBLE PRECISION,
        sms_scheduler_id BIGINT,
        is_sms_sent TEXT,
        email_scheduler_id BIGINT,
        is_email_sent TEXT,
        ticket_category TEXT,
        last_call_datetime TIMESTAMP,
        close_ticket TEXT,
        installment BIGINT,
        total_payment BIGINT,
        previous_payment BIGINT,
        previous_payment_date TIMESTAMP,
        remaining_dept BIGINT,
        promise_date TIMESTAMP,
        promise_target DOUBLE PRECISION
    );
    """)

    print("Các bảng đã được tạo thành công!")

if __name__ == "__main__":
    create_tables()