{{config(materialized='table')}}

with final as (

    select rating, category, count(*) as count
    from {{ ref('core_restaurants') }}
    where rating is not null
    group by category, rating

)

select * from final