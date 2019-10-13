from flask import Flask

app = Flask(__name__)


@app.route('/')
def pong():
    return 'pong'


@app.before_request
def log_before():
    print(1)
    # logging here


@app.after_request
def log_after(response):
    # logging here
    return response


if __name__ == '__main__':
    app.run()
