select
    order_id,
    count(*) as item_count,
    sum(price) as gross_item_value,
    sum(freight_value) as freight_value
from {{ ref('stg_olist__order_items') }}
group by 1