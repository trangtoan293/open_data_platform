WITH ticket_data AS (
    SELECT
        id as ticket_id,
        campaign_id,
        principal,
        dept,
        dpd,
        total_paid,
        status,
        created_date,
        updated_date
    FROM {{ ref('stg_ticket') }}
),

paired_data AS (
    SELECT
        ticket_id,
        SUM(cast(amt_paired as int)) AS total_amt_paired,
        COUNT(*) AS payment_count
    FROM {{ ref('stg_paired') }}
    GROUP BY ticket_id
)

SELECT
    t.ticket_id,
    t.campaign_id,
    t.principal,
    t.dept,
    t.dpd,
    t.total_paid,
    COALESCE(p.total_amt_paired, 0) AS total_amt_paired,
    COALESCE(p.payment_count, 0) AS payment_count,
    t.status,
    t.created_date,
    t.updated_date
FROM ticket_data t
LEFT JOIN paired_data p ON t.ticket_id = p.ticket_id