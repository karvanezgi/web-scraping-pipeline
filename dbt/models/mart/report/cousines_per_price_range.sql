{{config(materialized='table')}}

with final as (

    select category, price_range, count(*) as count
    from {{ ref('core_restaurants') }}
    group by category, price_range

)

select * from final