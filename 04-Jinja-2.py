from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h2>Helllo This is an integrated html flask page<h2></html>"

@app.route("/success/<int:score>",methods=['GET','POST'])
def success(score):
    if score>=35:
        res="passed"
    else:
        res="failed"
    return render_template('result.html', result=res)


 

@app.route("/successIFEL/<int:score>",methods=['GET','POST'])
def successIFEL(score):

    return render_template('resultIFEL.html', result=score)




if __name__ == "__main__":
    app.run(debug=True)