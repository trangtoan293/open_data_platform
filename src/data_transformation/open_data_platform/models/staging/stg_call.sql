with cte_source as (
    select * from {{ source('crm', 'airbyte_raw_cdr') }}
)
, parsed as ( 
    select 
    "_airbyte_emitted_at" as inserted_at
    ,_airbyte_data as data
    from cte_source
)
select 
inserted_at,
json_query(data, 'strict $.id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  id,
json_query(data, 'strict $.calldate'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  calldate,
json_query(data, 'strict $.clid'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  clid,
json_query(data, 'strict $.src'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  src,
json_query(data, 'strict $.dst'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  dst,
json_query(data, 'strict $.dcontext'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  dcontext,
json_query(data, 'strict $.channel'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  channel,
json_query(data, 'strict $.dstchannel'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  dstchannel,
json_query(data, 'strict $.lastapp'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  lastapp,
json_query(data, 'strict $.lastdata'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  lastdata,
json_query(data, 'strict $.duration'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  duration,
json_query(data, 'strict $.billsec'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  billsec,
json_query(data, 'strict $.disposition'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  disposition,
json_query(data, 'strict $.amaflags'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  amaflags,
json_query(data, 'strict $.accountcode'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  accountcode,
json_query(data, 'strict $.uniqueid'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  uniqueid,
json_query(data, 'strict $.userfield'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  userfield,
json_query(data, 'strict $.did'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  did,
json_query(data, 'strict $.recordingfile'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  recordingfile,
json_query(data, 'strict $.cnum'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  cnum,
json_query(data, 'strict $.cnam'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  cnam,
json_query(data, 'strict $.outbound_cnum'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  outbound_cnum,
json_query(data, 'strict $.outbound_cnam'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  outbound_cnam,
json_query(data, 'strict $.dst_cnam'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  dst_cnam,
json_query(data, 'strict $.project_code'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  project_code,
json_query(data, 'strict $.inbound_queue'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  inbound_queue,
json_query(data, 'strict $.campaign_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  campaign_id,
json_query(data, 'strict $.ticket_id'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  ticket_id,
json_query(data, 'strict $.inbound_agent'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  inbound_agent,
json_query(data, 'strict $.inbound_uid'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  inbound_uid,
json_query(data, 'strict $.call_route'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  call_route,
json_query(data, 'strict $.trunk_name'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  trunk_name,
json_query(data, 'strict $.contract_number'  WITHOUT  ARRAY WRAPPER OMIT QUOTES ) as  contract_number
from parsed

