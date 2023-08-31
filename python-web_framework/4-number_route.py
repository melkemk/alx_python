"""
This module is a simple Flask application that
provides greetings and routes for specific URLs.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return f'C {text.replace("_", " ")}'
    
@app.route('/python/<text>', strict_slashes=False)
def c_text(text):
    if text:
        return f'Python {text.replace("_", " ")}'
    else:
        return 'Python cool'
@app.route('/number/<n:int>', strict_slashes=False)
def c_text(n):
    if n==int(n):
        return f' {n} is number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
