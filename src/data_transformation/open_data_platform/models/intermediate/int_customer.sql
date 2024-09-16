WITH ticket_data AS (
    SELECT
        id,
        name,
        customer_type,
        mobile_phone,
        email,
        contract_number
    FROM {{ ref('stg_ticket') }}
)

SELECT DISTINCT
    id as contract_id,
    name,
    customer_type,
    mobile_phone,
    email,
    contract_number
FROM ticket_data