# Flask webserver framework
# Nothing built or functional yet
# TODO
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
