from flask import Flask
import _sqlite3
import sqlalchemy


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Oh hell World!'

@app.route('/', methods=['POST'])
def parse_request():
    data = request.data  # data is empty




if __name__ == '__main__':
    app.run()
