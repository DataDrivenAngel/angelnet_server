from flask import Flask
import _sqlite3
import sqlalchemy


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
