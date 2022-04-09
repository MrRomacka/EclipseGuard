import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/hey')
def Start():
    pass

@app.route('/', )
def FL():
    print('Hi')
    f = open('txt.txt', 'w')
    for arg in request.args:
        fr = request.args.get(arg[0])
        print(fr)
    return 'Hi, Mark'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
