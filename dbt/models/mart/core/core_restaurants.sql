
{{config(materialized='table')}}

with final as (

    select *
    from {{ ref('raw_zone_stg_users') }}

)

select * from final

-- can be changed to incremental model after first load

-- {{config(materialized='incremental')}}

-- with final as (
--     select *
--     from {{ ref('raw_zone_stg_users') }}
--     {% if is_incremental() %}
--     where id > (select max(id) from {{this}} )
--     {% endif %}
-- )

-- select * from final


