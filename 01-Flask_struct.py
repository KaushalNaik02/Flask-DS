
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask framework... Also This is an Amazing framework"

@app.route("/index")
def index():
    return "Welcome to the index page"

@app.route("/index/home")
def home():
    return "Welcome to the home page"


if __name__ == "__main__":
    app.run(debug=True)        # Here "dubug = true" helps to reload the page without restarting server after updating/changes in page 
