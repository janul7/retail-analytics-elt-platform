select
    customer_id,
    count(distinct order_id) as total_orders,
    sum(total_payment_amount) as lifetime_value
from {{ ref('fct_orders') }}
group by 1