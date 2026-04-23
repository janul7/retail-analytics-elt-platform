select
    product_category_name,
    product_category_name_english,
    _loaded_at
from {{ source('raw_olist', 'category_translation') }}