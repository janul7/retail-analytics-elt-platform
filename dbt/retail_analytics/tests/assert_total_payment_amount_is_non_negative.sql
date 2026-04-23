select *
from {{ ref('fct_orders') }}
where total_payment_amount < 0