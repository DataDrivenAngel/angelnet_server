from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.route('/')
# def hello_world():
#     return 'Oh hell World!'


@app.post("/input")
def input(data):
    # data = request.data  # data is empty
    print(Header(data))



if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.2", port=8000)