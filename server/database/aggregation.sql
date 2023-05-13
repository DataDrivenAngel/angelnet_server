BEGIN;

WITH minutely AS (
    SELECT
        node_id,
        min (temp) AS temp_min,
        avg (temp) AS temp_avg,
        percentile(0.5) as temp_median,
        max (temp) AS temp_max
    FROM sensor_data_raw
    WHERE hour(load_timestamp) < hour(current_timestamp)
    GROUP BY node_id

)

INSERT INTO sensor_minute SELECT * FROM minutselectely;

delete * from sensor_data_raw where hour(load_timestamp) > current_timestamp;
commit;
