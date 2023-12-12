{{ config(materialized='table') }}

with final as (

    select *
    from {{ source('raw_zone', 'restaurants') }}

)

select * from final
