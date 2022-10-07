from flask import Flask, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "hello, world"


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 80)
