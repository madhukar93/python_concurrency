# server.py
import time
import threading
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    # Will not block the entire app if multithreaded
    time.sleep(1)  # take about 1 s
    return f"Hello, World!, I am thread {threading.current_thread().name}"


app.run()  # TODO: enable threading
