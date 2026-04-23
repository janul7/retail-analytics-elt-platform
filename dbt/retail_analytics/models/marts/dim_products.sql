select
    p.product_id,
    p.product_category_name,
    t.product_category_name_english
from {{ ref('stg_olist__products') }} p
left join {{ ref('stg_olist__category_translation') }} t
    on p.product_category_name = t.product_category_name