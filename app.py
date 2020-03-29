from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World!'

@app.route('/<name>')
def hello(name)
    return f'Hello,{name}!'

@app.route('/double/<number>')
def double(number):
    return str(2*int(number))
    