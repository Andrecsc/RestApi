from flask import Flask, render_template, jsonify
import json
import requests
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "uwu"


@app.route('/getstores')
def get_store():  # put application's code here
    req = requests.get("http://127.0.0.1:5000/store")
    data = json.loads(req.content)
    return render_template('file1.html', data=data)


@app.route('/poststore', methods=['POST'])
def post_store():  # put application's code here
    store_name: str = "store 2"
    item_name: str = "item 2"
    item_price: float = 12.99

    payload = {'name': store_name, 'item': [{'name': item_name, 'price': item_price}]}
    jsonify(payload)

    req = requests.post("http://127.0.0.1:5000/store1", json=payload)

    return render_template("poststore.html", message = str(req.text))


if __name__ == '__main__':
    app.run()

