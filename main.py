from fastapi import FastAPI, Header
import uvicorn
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
    uvicorn.run(app, host="192.168.1.2", port=8000)