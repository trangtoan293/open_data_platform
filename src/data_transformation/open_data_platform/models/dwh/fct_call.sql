SELECT
    id as call_id,
    calldate,
    src,
    dst,
    duration,
    disposition,
    campaign_id,
    ticket_id,
    inbound_agent
FROM {{ ref('stg_call') }}