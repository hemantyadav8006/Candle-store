from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

app = Flask(__name__)
uri = "mongodb+srv://hemantyadav8006:wNqvrptyynTzSuky@cluster2.nnrkaax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2"

client  = MongoClient(uri)

db = client.candle_store

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/candle-store', methods=['GET'])
def candle_store_get():
    candlelist = list(db.candlelist.find({}, {'_id': False}))
    return jsonify({'candlelist':candlelist})



@app.route('/candle-store', methods=['POST'])
def candle_store():
    
    username = request.form['username']
    Quantity = request.form['Quantity']
    Address = request.form['Address']
    Phone_Number = request.form['Phone_Number']
    # print(username,Quantity,Address,Phone_Number)
    db.candlelist.insert_one({
        'username': username,
        'Quantity': Quantity,
        'Address' : Address,
        'Phone_Number': Phone_Number
    })
    
    return jsonify({'msg':'Order Placed Successfully!'})



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

