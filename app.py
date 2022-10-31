from flask import Flask

app = Flask(__name__)

def home():
    return 'Hello, Web'

app.run()