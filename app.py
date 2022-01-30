from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hi there!</h1>'

@app.route('/about')
def about():
    return '<h2>This is solely for demo</h2>'

@app.route('/greet')
def greet():
    return '<h1>Hope you have a great day ahead!</h1>'