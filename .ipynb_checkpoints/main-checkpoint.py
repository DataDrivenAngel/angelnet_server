from fastapi import FastAPI, Header
import uvicorn
from config import local_ip, db_url, dbname
import time
import sqlalchemy

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/input")
def read_data(device_id: str, temp = float, humid = float, light = float,):
    # data = request.data  # data is empty
    print(time.time())
    print(device_id)
    print(temp)
    print(humid)
    print(light)



    return("received")



if __name__ == "__main__":
    uvicorn.run(app, host=local_ip, port=8000)