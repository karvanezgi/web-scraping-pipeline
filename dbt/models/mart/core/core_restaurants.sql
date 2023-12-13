
{{config(materialized='table')}}

with final as (

    select r.id, r.name, r.category, r.price_range, CASE WHEN r.rating='' then null else r.rating END as rating, CURRENT_DATE as ingestion_date
    from {{ ref('stg_restaurants') }} as r

)

select * from final

-- can be changed to incremental model after first load

-- {{config(materialized='incremental')}}

-- with final as (
--     select r.name, r.category, r.price_range, CASE WHEN r.rating='' then null else r.rating END as rating, CURRENT_DATE as ingestion_date
--     from {{ ref('stg_restaurants') }} r
--     {% if is_incremental() %}
--     where id > (select max(id) from {{this}} )
--     {% endif %}
-- )

-- select * from final


