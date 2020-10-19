import time

from flask import Flask
from multiprocessing import Process, freeze_support

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def run_flask_app():
    app.run()


def run_process():
    freeze_support()

    a = Process(target=run_flask_app)
    a.daemon = True
    a.start()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    while True:
        print("lol")
        time.sleep(1)
