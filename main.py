import fastapi
import uvicorn
from config import local_ip, dbname, dbuser, dbpassword, dbhost, dbport
import datetime
from pg import DB
from typing import Optional
import urllib.request as urllib2
import json



app = fastapi.FastAPI()

# connect to DB
try:
    db = DB(dbname=dbname, host=dbhost, port=dbport, user=dbuser, passwd=dbpassword)
except:
    print("db error")


@app.get("/")
async def root():
    return {"message": "Oh Hell World"}

@app.post("/input")
def read_data(device_id: str, temp: Optional[float], humid: Optional[float], light: Optional[float]):

    db = DB(dbname=dbname, host=dbhost, port=dbport, user=dbuser, passwd=dbpassword)
    table = "raw_data"
    local_received_time = datetime.datetime.utcnow()

    insert_statement = f"""INSERT INTO {table} (device_id,temp,humidity,light,timestamp_on_write)
                        VALUES ('{device_id}',{temp},{humid},{light},'{local_received_time}');
                        """

    # Write to PGDB
    try:
        db.query(insert_statement)
    except:
        pass


    # Push to Power BI
    # try:
    payload = f"""
        [{{
            "DateTime" :"{local_received_time}",
            "Temperature" :{temp},
            "Humidity" :{humid},
            "Brightness" :{light},
            "Device" :"{device_id}"
        }}]
        """
    body = bytes(payload, encoding='utf-8')
    http_req = urllib2.Request(streaming_url, body)
    response = urllib2.urlopen(http_req)

    # except:
    #     print("POST request to Power BI with data:{0}".format(body))
    #     print("PBI ERROR")
    # return ("received")


# @app.get("/test")
# def test_db_conn():
#
#     device_id = "test_device_id"
#     temp = "25.20"
#     humid = "31.00"
#     light = "0.10"
#     local_received_time = time.time()
#     table = "raw_data"
#     conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, port=dbport, host=dbhost)
#     insert_statement = f"""INSERT INTO {table} (device_id,temp,humid,light,local_received_time)
#                         VALUES ({device_id},{temp},{humid},{light},{local_received_time});
#                         """
#     return (conn)


if __name__ == "__main__":
    uvicorn.run(app, host = local_ip, port=8000)
