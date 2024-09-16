SELECT
    contract_id AS ticket_id,
    row_number() over (partition by contract_id) as customer_id,
    name,
    customer_type,
    mobile_phone,
    email,
    contract_number
FROM {{ ref('int_customer') }}