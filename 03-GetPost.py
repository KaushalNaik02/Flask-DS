from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h2>Helllo This is an integrated html flask page<h2></html>"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
       name = request.form['name']
       return f"Hello {name}!! Welcome to our website"
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
       name = request.form['name']
       return f"Hello {name}!! Welcome to our website"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)