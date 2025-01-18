from flask import Flask
from flask import jsonify


app = Flask(__name__)



items = [
    {"id":01, "name":"Product1","Description":"This is Product1"},
    {"id":02, "name":"Product2","Description":"This is Product2"}

]

@app.route('/')
def home():
    return "Welcome to my API"

# GET: Retriveing all elements

# @app.route('/get_items',method=['GET'])
# def get_items():
#     return jsonify(items)

# GET: Retriveing specific elements

@app.route('/get_items/<int:item_id>',method=['GET'])
def get_items(item_id):
    item = next((item for item in items if items['id'] == item_id), None)
    if item is None:
        return jsonify("Item N ot Found")
    return jsonify(item)



if __name__ == "__main__":
    app.run(debug=True)




# This Is An Incomplete Task        