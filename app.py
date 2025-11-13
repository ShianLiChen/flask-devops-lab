from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, DevOps World!'


@app.route('/motivator')
def motivator():
    quotes = [
        "Keep pushing forward!",
        "CI/CD saves the day!",
        "Automate all the things!",
        "Commit early, commit often!",
        "Fail fast, learn faster!"
    ]
    return random.choice(quotes)


if __name__ == '__main__':
    app.run()
