with cte_source as (
    select * from {{ source('crm', 'airbyte_raw_paired') }}
)
, parsed as ( 
    select 
    "_airbyte_emitted_at" as inserted_at
    ,_airbyte_data as data
    from cte_source
)
select 
    inserted_at,
    json_query(data, 'strict $.ticket_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  ticket_id,
json_query(data, 'strict $.amt_paired'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  amt_paired,
json_query(data, 'strict $.date_paired'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  date_paired,
json_query(data, 'strict $.employee_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  employee_id
from parsed

