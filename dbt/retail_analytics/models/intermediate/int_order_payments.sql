select
    order_id,
    sum(payment_value) as total_payment_amount,
    max(payment_installments) as max_payment_installments
from {{ ref('stg_olist__payments') }}
group by 1