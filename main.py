from fastapi import FastAPI, Header
import uvicorn
from config import local_ip
import sqlalchemy

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/input")
def read_data(device_id: str, values = None):
    # data = request.data  # data is empty

    print(device_id)
    print(values)

    return("received")



if __name__ == "__main__":
    uvicorn.run(app, host=local_ip, port=8000)