from flask import Flask

#define app for flask
app = Flask(__name__)

#creating app route
@app.route('/')
def hello_world():
    return 'Hello World!'