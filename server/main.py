import fastapi
import uvicorn
from config import local_ip, dbname, dbuser, dbpassword, dbhost, dbport
import datetime
from pg import DB
from typing import Optional
import urllib.request as urllib2
import json

app = fastapi.FastAPI()

from prometheus_fastapi_instrumentator import Instrumentator
Instrumentator().instrument(app).expose(app)

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

    # Write to PG DB
    try:
        db.query(insert_statement)
    except:
        pass

if __name__ == "__main__":
    uvicorn.run(app, host = local_ip, port=8000)
