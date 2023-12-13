{{config(materialized='table')}}

with final as (

    select 
    category, 
    ingestion_date, 
    count(*) as count
    from {{ ref('core_restaurants') }}
    group by category, ingestion_date

)

select * from final