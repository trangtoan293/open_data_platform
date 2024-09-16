with cte_source as (
    select * from {{ source('crm', 'airbyte_raw_campaign') }}
)
, parsed as ( 
    select 
    "_airbyte_emitted_at" as inserted_at
    ,_airbyte_data as data
    from cte_source
)
select 
    inserted_at,
    json_query(data, 'strict $.campaign_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  campaign_id,
    json_query(data, 'strict $.name'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  name,
    json_query(data, 'strict $.description'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  description,
    json_query(data, 'strict $.time_limit'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  time_limit,
    json_query(data, 'strict $.status'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  status,
    json_query(data, 'strict $.type'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  type,
    json_query(data, 'strict $.is_call_type'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  is_call_type,
    json_query(data, 'strict $.is_sms_type'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  is_sms_type,
    json_query(data, 'strict $.is_email_type'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  is_email_type,
    json_query(data, 'strict $.start_date'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  start_date,
    json_query(data, 'strict $.end_date'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  end_date,
    json_query(data, 'strict $.dialer_type'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  dialer_type,
    json_query(data, 'strict $.predictive_dialer_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  predictive_dialer_id,
    json_query(data, 'strict $.survey_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  survey_id,
    json_query(data, 'strict $.created_by'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  created_by,
    json_query(data, 'strict $.created_date'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  created_date,
    json_query(data, 'strict $.import_status'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  import_status,
    json_query(data, 'strict $.sms_scheduler_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  sms_scheduler_id,
    json_query(data, 'strict $.sms_run_status'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  sms_run_status,
    json_query(data, 'strict $.email_scheduler_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  email_scheduler_id,
    json_query(data, 'strict $.email_run_status'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  email_run_status,
    json_query(data, 'strict $.ticket_type_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  ticket_type_id,
    json_query(data, 'strict $.notice_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  notice_id
from parsed
