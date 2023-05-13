import streamlit as st
import sys
import sqlalchemy
import pandas as pd
import datetime
import altair
from config import local_ip, dbname, dbuser, dbpassword, dbhost, dbport


st.title("Angel Net Data")
last_refresh_time = datetime.datetime.utcnow()
st.write(f"Last Refreshed at: {last_refresh_time}" )

# connect to DB
try:
    engine = sqlalchemy.create_engine(f"postgresql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")
    
except:
    st.write("db error")

heartbeat_sql = f"""

select max(timestamp_on_write) as last_seen
, device_id
from raw_data
where device_id in ('Window','Kitchen','Bedroom')
group by device_id

             """

with engine.connect() as conn:
    heartbeat_data = pd.read_sql_query(con = conn, sql = heartbeat_sql)

st.header("Heartbeat data")
st.write(heartbeat_data)



last_hour_chart_sql = f"""

select timestamp_on_write as time
, temp
, humidity
, light
, device_id
from raw_data
where timestamp_on_write >= NOW() - '1 hour' ::INTERVAL


             """
with engine.connect() as conn:
    temp_data = pd.read_sql_query(con = conn, sql = last_hour_chart_sql)

st.header("Last Hour")
st.subheader("Temperature data (degrees c)")
temp_chart = altair.Chart(temp_data).mark_line().encode(x = 'time', y = 'temp', color = 'device_id')
st.write(temp_chart)

st.subheader("Humidity data (%)")
humidity_chart = altair.Chart(temp_data).mark_line().encode(x = 'time', y = 'humidity', color = 'device_id')
st.write(humidity_chart)

st.subheader("Light data (%)")
light_chart = altair.Chart(temp_data).mark_line().encode(x = 'time', y = 'light', color = 'device_id')
st.write(light_chart)

db_size = f"""

select count(*) from raw_data
             """
with engine.connect() as conn:
    rows = pd.read_sql_query(con = conn, sql = db_size)

st.header("number of rows:")
st.write(rows)