from flask import Flask
from flask import request
import _sqlite3
import sqlalchemy


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Oh hell World!'

@app.route('/input', methods=['POST'])
def input():
    if request.method == 'POST':
        app.logger.debug('post!')
        app.logger.debug(request.data)
        app.loger.debug(request.data.temp)
        return 'posted!'

    else:
        app.logger.debug('no post')
        return 'no post'
    app.logger.debug('logging')
     #data = request.data  # data is empty





if __name__ == '__main__':
    app.run()
