from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Helllo This is an integrated html flask page<h2></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)