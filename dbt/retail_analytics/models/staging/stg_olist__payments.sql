select
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value,
    _loaded_at
from {{ source('raw_olist', 'payments') }}