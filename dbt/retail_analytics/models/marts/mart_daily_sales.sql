select
    order_date,
    count(*) as total_orders,
    sum(total_payment_amount) as total_revenue,
    avg(total_payment_amount) as avg_order_value
from {{ ref('fct_orders') }}
where order_status = 'delivered'
group by 1