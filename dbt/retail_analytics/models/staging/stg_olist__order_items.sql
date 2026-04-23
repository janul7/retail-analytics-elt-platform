select
    order_id,
    order_item_id,
    product_id,
    seller_id,
    cast(shipping_limit_date as timestamp) as shipping_limit_ts,
    price,
    freight_value,
    _loaded_at
from {{ source('raw_olist', 'order_items') }}