from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi Prem"

@app.route("/hello")
def greet():
    return "Hi Prem How are you"

if __name__ == "__main__":
    app.run()

