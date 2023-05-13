BEGIN

with minutely as (
    select 
        node_id
        min(temp)
        avg(temp),
        max(temp),
    from
    sensor_data_raw
    group by node_id
    where load_timestamp > current_timestamp.

)

insert into sensor_minute select * from minutely. 

delete select * from sensor_data_raw where load_timestamp > current_timestamp
