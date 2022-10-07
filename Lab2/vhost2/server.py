from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
    return "hello, world 2"

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)


