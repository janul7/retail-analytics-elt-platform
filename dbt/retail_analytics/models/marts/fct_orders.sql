with orders as (
    select * from {{ ref('stg_olist__orders') }}
),
items as (
    select * from {{ ref('int_order_items') }}
),
payments as (
    select * from {{ ref('int_order_payments') }}
)

select
    o.order_id,
    o.customer_id,
    date(o.order_purchase_ts) as order_date,
    o.order_status,
    coalesce(i.item_count, 0) as item_count,
    coalesce(i.gross_item_value, 0) as gross_item_value,
    coalesce(i.freight_value, 0) as freight_value,
    coalesce(p.total_payment_amount, 0) as total_payment_amount,
    coalesce(p.max_payment_installments, 0) as max_payment_installments
from orders o
left join items i
    on o.order_id = i.order_id
left join payments p
    on o.order_id = p.order_id