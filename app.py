from distutils.command import install
from os import pipe

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

http://127.0.0.1:5000/
